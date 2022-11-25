from rest_framework import serializers
from shipping_app.models import *


class CouriersCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CouriersCompany
        fields = ['id', 'company_id', 'courier_name', 'image_url']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'carrier_id', 'awb', 'order_id', 'first_name', 'last_name', 'email', 'phone', 'product_desc', 'company']