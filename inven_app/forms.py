from django import forms
from .models import Orgnaiztion_add,ProductName

class OrganizationAddForm(forms.ModelForm):
    class Meta:
        model = Orgnaiztion_add
        fields = '__all__'
        widgets = {
            'Organization_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter organization name'
            }),
            'adress': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address'
            }),
            'Phone_Number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact person name'
            }),
            'Logo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductName
        fields = '__all__'

        widgets = {
            'Product_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'Type_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter type'
            }),
            'Size': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter size'
            }),
            'Category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'Color_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter color name'
            }),
            'Pack_Size': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pack size'
            }),
            'Reorder_Quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter reorder qty'
            }),
            'Sequence': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter sequence'
            }),
            'Is_Raw_Material': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
           
        }

        labels = {
            'Product_Name': 'Product Name',
            'Type_Name': 'Type',
            'Size': 'Size',
            'Category': 'Category',
            'Color_Name': 'Color',
            'Pack_Size': 'Pack Size',
            'Reorder_Quantity': 'Reorder Quantity',
            'Sequence': 'Sequence',
            'Is_Raw_Material': 'Raw Material',
            
        }
class ProductSearchForm(forms.Form):
    product_type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Type'})
    )
    product_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Name','autocomplete': 'off',
            'id': 'product-search'})
    )
    is_raw_material = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','onchange': 'this.form.submit()'}),
        label="Is Raw Material?"
    )     