from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from inven_app.models import *

# Register your models here.
admin.site.register(Production_Entry)
admin.site.register(Orgnaiztion_add)
admin.site.register(ProductName)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone", "designation")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone", "designation")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
