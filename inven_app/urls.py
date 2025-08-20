from django.urls import path
from inven_app.views import *
urlpatterns =[
    path('home/',home,name='home'),

    path('Production_Entry/',ProductionEntry,name='pde'),

    path('Organaization Add/',Organaization_add,name='orga_add'),
    path('Product/',Product,name='Product'),
    path('Addproduct/',Addproduct,name='Addproduct'),
    path("product/<int:pk>/update/", product_update, name="update_p"),
    path("product/<int:pk>/delete/", product_delete, name="delete_p"),
    path('products-autocomplete/', product_autocomplete, name='product_autocomplete'),
    path("not-raw-autocomplete/", not_raw_autocomplete, name="not_raw_autocomplete"),


    path('User/',User_list,name='user'),
    path('AddUser/',User_add,name='adduser'),
    path('',Login_,name='login'),
    path('logout/', Logout_, name='logout'),
    path('Signup/',SignUP_,name='signup'),

    path('Organization/',Organization,name='organization'),

    path('Add_productionentry/',Add_production,name='Apde'),

    path('Export-production/',Export_Productiondata_excel, name='export_production'),
]













