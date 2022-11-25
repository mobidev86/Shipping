from django.contrib import admin
from shipping_app.models import *
# Register your models here.


@admin.register(CouriersCompany)
class CouriersCompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_id', 'courier_name', 'image_url']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'awb', 'order_id', 'first_name', 'last_name', 'email', 'status']