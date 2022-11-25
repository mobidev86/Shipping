from django.contrib import admin
from django.urls import path, include
from shipping_app import views

urlpatterns = [

    path("create-waybill/", views.ShipwayShippinMethod.create_waybill, name='create_waybill'),

    path("print-waybill-label/", views.ShipwayShippinMethod.print_waybill_label, name='print_waybill_label'),

    path("get-status/", views.ShipwayShippinMethod.get_status, name='get_status'),
]
