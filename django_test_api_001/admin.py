from django.contrib import admin

# Register your models here.

from .models import Employee, Client, Product, Order, Statistic


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birthdate')
    list_filter = ('full_name', 'birthdate')
    # list_editable = ('full_name', 'birthdate')

admin.site.register(Employee, EmployeeAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birthdate')
    list_filter = ('full_name', 'birthdate')
    # list_editable = ('full_name', 'birthdate')

admin.site.register(Client, ClientAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    list_filter = ('name', 'quantity', 'price')
    # list_editable = ('name', 'quantity', 'price')


admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('сlient', 'employee', 'created_date')
    list_filter = ('сlient', 'product', 'employee', 'created_date')
    # list_editable = ('сlient', 'product', 'employee', 'created_date')
    list_editable = ('employee', 'created_date')

admin.site.register(Order, OrderAdmin)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('full_name_employee', 'employee', 'client', 'full_name_client', 'quantity_clients', 'quantity_products', 'total_price', 'created_date')


    list_filter = ('full_name_employee', 'employee', 'client', 'full_name_client', 'quantity_clients', 'quantity_products', 'total_price', 'created_date')
    list_editable = ('client', 'full_name_client', 'quantity_clients', 'quantity_products', 'total_price', 'created_date')

admin.site.register(Statistic, StatisticAdmin)







