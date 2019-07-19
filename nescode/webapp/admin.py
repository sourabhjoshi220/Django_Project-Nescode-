from django.contrib import admin
from webapp.models import customer, investment

# Register your models here.

class first_admin(admin.ModelAdmin):
    list_display = ['Name','Add','Phone_no','Email']

admin.site.register(customer,first_admin)

class second_admin(admin.ModelAdmin):
    list_display = ['Customer_Name','Amount','Investment_Type']
admin.site.register(investment,second_admin)
