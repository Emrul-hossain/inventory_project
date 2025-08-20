from django.db import models
from django.contrib.auth.models import AbstractUser

from inven_app.manager import CustomUserManager

# Create your models here.
class Production_Entry(models.Model):
    UNIT_CHOICES = [
        ('unit 1', 'unit 1'),
        ('unit 2', 'unit 2'),
        ('unit 3', 'unit 3'),
        ('unit 4', 'unit 4'),
        ('unit 5', 'unit 5'),
    ]
    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    Production_Entry_Date=models.DateField()
    select_unit=models.CharField(max_length=50,choices=UNIT_CHOICES)
    Entry_by=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_size=models.CharField(max_length=50,choices=SIZE_CHOICES)
    Total_Production=models.IntegerField()
    Total_Qualified=models.IntegerField()
    Total_Wastage=models.IntegerField()
    def __str__(self):
        return f"{self.select_unit}  {self.Entry_by}  {self.product_name}   {self.product_size}  {self.Total_Production}  {self.Total_Qualified}  {self.Total_Wastage} "

class Orgnaiztion_add(models.Model):
    Organization_name=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    Phone_Number= models.IntegerField()
    email=models.EmailField( max_length=254)
    contact_person=models.CharField( max_length=100)
    Logo=models.ImageField(upload_to='image/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"{self.Organization_name}  {self.adress}  {self.Phone_Number}   {self.email}  {self.contact_person}  {self.Logo}   "

class CustomUser(AbstractUser):
     phone= models.CharField(max_length=15, blank=True, null=True)
     designation=models.CharField(max_length=100)

     objects = CustomUserManager()

     def __str__(self):
         return self.username



class ProductName(models.Model):
   CATEGORY_CHOICES= [
        ('Cloth diapers', 'Cloth diapers'),
        ('Disposable diapers', 'Disposable diapers'),
        ('Swim diapers', 'Swim diapers'),
        ('New born', 'New born'),
        ('Small (4-8 kg) diapers', 'Small (4-8 kg) diapers'),
        ('Pant Style diapers', 'Pant Style diapers'),
        ('Washable Diaper', 'Washable Diaper'),
        ('Xxl (14-25 kg) diapers', 'Xxl (14-25 kg) diapers'),
    ]
   Product_Name=models.CharField(max_length=300)
   Type_Name=models.CharField( max_length=150)
   Size=models.IntegerField()
   Category=models.CharField( max_length=200,choices=CATEGORY_CHOICES )
   Color_Name=models.CharField( max_length=100)
   Pack_Size=models.IntegerField()
   Reorder_Quantity=models.IntegerField()
   Sequence=models.IntegerField()
   Is_Raw_Material=models.BooleanField()
   
 
   
   def __str__(self):
       return f"{self.Product_Name} {self.Type_Name} {self.Size} {self.Category}"
