from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from inven_app.forms import OrganizationAddForm
from inven_app.models import Orgnaiztion_add, ProductName, Production_Entry
from openpyxl import Workbook
from django.http import JsonResponse
from django.db.models import Sum
from .forms import ProductForm,ProductSearchForm
from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()

def home(request):
    return render(request,'home.html',)
class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductName
        fields = '__all__'
        widgets = {
            'Product_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Type_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Size': forms.NumberInput(attrs={'class': 'form-control'}),
            'Category': forms.TextInput(attrs={'class': 'form-control'}),
            'Color_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Pack_Size': forms.NumberInput(attrs={'class': 'form-control'}),
            'Reorder_Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Sequence': forms.NumberInput(attrs={'class': 'form-control'}),
            'Is_Raw_Material': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

# Update
def product_update(request, pk):
    product = get_object_or_404(ProductName, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("Product")
    else:
        form = ProductForm(instance=product)
    return render(request, "NameOf_product/update_p.html", {"form": form})



# Delete
def product_delete(request, pk):
    product = get_object_or_404(ProductName, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("Product")
    return render(request, "NameOf_product/delete_p.html", {"product": product})



def Product(request):
    form = ProductSearchForm(request.GET or None)
    products = ProductName.objects.all()   

    if form.is_valid():
        product_type = form.cleaned_data.get('product_type')
        product_name = form.cleaned_data.get('product_name')
        is_raw_material = form.cleaned_data.get('is_raw_material')

        if product_type:
            products = products.filter(Type_Name__icontains=product_type)   
        if product_name:
            products = products.filter(Product_Name__icontains=product_name)  
        if is_raw_material:
            products = products.filter(Is_Raw_Material=True)   

    return render(request, "NameOf_product/product.html", {"form": form, "products": products})



def product_autocomplete(request):
    term = request.GET.get('term', '')
    if term:
        qs = ProductName.objects.filter(Product_Name__icontains=term)[:10]  # limit 10
        names = list(qs.values_list('Product_Name', flat=True))
        return JsonResponse(names, safe=False)
    return JsonResponse([], safe=False)

def not_raw_autocomplete(request):
    if 'term' in request.GET:
        qs = ProductName.objects.filter(
            Product_Name__icontains=request.GET.get('term'),
            Is_Raw_Material=False
        )
        names = list(qs.values_list('Product_Name', flat=True))
        return JsonResponse(names, safe=False)
    return JsonResponse([], safe=False)

def Addproduct(request):
   if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
          form.save()
        return redirect("Addproduct")  
   else:
     form = ProductForm()

     return render(request, "NameOf_product/add_product.html", {"form": form})
   



   
def User_add(request):
    if request.method == "POST":
        name = request.POST.get('user_n')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        designation = request.POST.get('Designation')
        password = request.POST.get('password')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        elif User.objects.filter(phone=phone).exists():
            messages.error(request, "Phone already registered")
        else:
            user = User.objects.create_user(
                username=name,
                email=email,
                phone=phone,
                designation=designation,
                password=password
            )
            messages.success(request, "Account created successfully. Please login.")
            return redirect('user') 
    return render(request,'User/user_add.html')



def User_list(request):
    User_data=User.objects.all()
    
    
    return render(request,'User/user.html',{"u_data":User_data})



# login & signup view function
def Login_(request):
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



def Logout_(request):
    logout(request)  
    return redirect('login')



def SignUP_(request):
    if request.method == "POST":
        name = request.POST.get('user_n')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        designation = request.POST.get('Designation')
        password = request.POST.get('password')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        elif User.objects.filter(phone=phone).exists():
            messages.error(request, "Phone already registered")
        else:
            user = User.objects.create_user(
                username=name,
                email=email,
                phone=phone,
                designation=designation,
                password=password
            )
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')  

    return render(request, 'signup.html')




def Organization(request):
    Orga_data=Orgnaiztion_add.objects.all()
    return render(request,'ORGANIZATION/organization.html',{'Orga_data': Orga_data,})


def Organaization_add(request):
    
    if request.method == "POST":
        form = OrganizationAddForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('organization') 
    else:
        form = OrganizationAddForm()

    return render(request, 'ORGANIZATION/orga_add_form.html', {'form': form,})




def ProductionEntry(request):
    databy_id=request.POST.get('entry')
    # advanced search query
    unit_filter=request.POST.get("unit")
    product_name_filter=request.POST.get("product")
    size_filter=request.POST.get("size")
    start_date=request.POST.get("from")
    End_date=request.POST.get("to")

    results = Production_Entry.objects.none() 

    # Only run query if there is a search or filter
    if databy_id or unit_filter or size_filter or (start_date and End_date):
        results = Production_Entry.objects.all()
    # filter by id
    if databy_id:
        results=results.filter(id=databy_id)

    # filter by unit 
    if unit_filter:
        results=results.filter(select_unit=unit_filter)

    # filter by name
    if product_name_filter:
        product_name_filter = product_name_filter.strip()
        results=results.filter(product_name__iexact=product_name_filter)
    # Filter by size
    if size_filter:
        results=results.filter(product_size=size_filter)
    # Filter by date
    if start_date and End_date:
        results=results.filter(Production_Entry_Date__range=[start_date,End_date])

    total_production = results.aggregate(total_sum=Sum('Total_Production'))['total_sum'] or 0
    total_qualified = results.aggregate(total_sum=Sum('Total_Qualified'))['total_sum'] or 0
    total_wastage = results.aggregate(total_sum=Sum('Total_Wastage'))['total_sum'] or 0


    return render(request,'productionentry.html',{'results': results,
        'id_query': databy_id,
        'unit_filter': unit_filter,
        'size_filter': size_filter,
        'start_date': start_date,
        'end_date': End_date,
        'total_production': total_production,
        'total_qualified': total_qualified,
        'total_wastage': total_wastage,})
def Add_production(request):
    if request.method == "POST":
        p_entry_date = request.POST.get('date')
        production_unit = request.POST.get('production_unit')
        
        product_name = request.POST.get('Product-Name')
        product_size = request.POST.get('product_size')
        total_production = int(request.POST.get('total-p', 0))
        total_qualified = int(request.POST.get('total-Q', 0))
        total_wastage = int(request.POST.get('total-w', 0))


        # Auto-calculate wastage
        
        if total_qualified + total_wastage != total_production:
            return JsonResponse({
                'status': 'error',
                'message': '❌ Total Qualified + Total Wastage must equal Total Production.'
            })
        entry_by = request.user.username
        obj = Production_Entry(
            Production_Entry_Date=p_entry_date,

            select_unit=production_unit,
            Entry_by=entry_by,
            product_name=product_name,
            product_size=product_size,
            Total_Production=total_production,
            Total_Qualified=total_qualified,
            Total_Wastage=total_wastage
        )
        obj.save()
        return JsonResponse({'status': 'success', 'message': '✅ Data saved successfully!'})
        

    return render(request, 'add_production.html')
def Export_Productiondata_excel(request):
    databy_id=request.POST.get('entry')
    # advanced search query
    unit_filter=request.POST.get("unit")
    product_name_filter=request.GET.get("product")
    size_filter=request.POST.get("size")
    start_date=request.POST.get("from")
    End_date=request.POST.get("to")

    results=Production_Entry.objects.all()

    # filter by id
    if databy_id:
        results=results.filter(id=databy_id)

    # filter by unit 
    if unit_filter:
        results=results.filter(select_unit=unit_filter)

    # filter by name
    if product_name_filter:
        results=results.filter(product_name=product_name_filter)
    # Filter by size
    if size_filter:
        results=results.filter(product_size=size_filter)
    # Filter by date
    if start_date and End_date:
        results=results.filter(Production_Entry_Date__range=[start_date,End_date])

    # Create an Excel workbook 
    wb=Workbook()
    ws=wb.active   
    ws.title= 'Production Data'

    # header row
    ws.append([
        'ID', 'Entry Date', 'Unit', 'Entry By', 'Product Name',
        'Size', 'Total Production', 'Qualified', 'Wastage'
    ])
    # Data rows
    for item in results:
        ws.append([
            item.id,
            str(item.Production_Entry_Date),
            item.select_unit,
            item.Entry_by,
            item.product_name,
            item.product_size,
            item.Total_Production,
            item.Total_Qualified,
            item.Total_Wastage
        ])

        # Create HTTP response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="production_data.xlsx"'
    wb.save(response)

    return response


    
