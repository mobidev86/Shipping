import requests
import json
from django.conf import settings
from rest_framework.views import APIView
from shipping_app.models import CouriersCompany
from shipping_app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from shipping_app.shipping_method import ShippingMethod
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Fetch Shipway username and password from env
SHIPWAY_USERNAME = getattr(settings, "SHIPWAY_USERNAME", "")
SHIPWAY_KEY = getattr(settings, "SHIPWAY_KEY", "")


def getHeaders():
    headers = {
        'Content-Type': 'application/json'
        }
    return headers

def getValues():
    values = {
        "username": SHIPWAY_USERNAME,
        "password": SHIPWAY_KEY
    }
    return values


# This class used for create new order


@method_decorator(csrf_exempt, name='dispatch')
class ShipwayShippinMethod(ShippingMethod, APIView):
    order_id = None
    carrier_id = None
    awb = None
    first_name = None
    last_name = None
    email = None
    phone = None
    products = None
    company = None

    def __init__(self, order_id, carrier_id=None, awb=None, first_name=None, last_name=None, email=None, phone=None, products=None, company=None):
        self.order_id = order_id
        ShipwayShippinMethod.carrier_id = carrier_id
        ShipwayShippinMethod.awb = awb
        ShipwayShippinMethod.first_name = first_name
        ShipwayShippinMethod.last_name = last_name
        ShipwayShippinMethod.email = email
        ShipwayShippinMethod.phone = phone
        ShipwayShippinMethod.products = products
        ShipwayShippinMethod.company = company

    def post(self, request, format=True):
        order_data = request.data

    @csrf_exempt
    @api_view(('POST',))
    def create_waybill(self):
        print("Waybill printed")
        return Response({"status": "Success"}, status=status.HTTP_200_OK)
        
        #Actual implementation will look like below code
        # values = {
        #     "username": SHIPWAY_USERNAME,
        #     "password": SHIPWAY_KEY,
        #     "carrier_id": ShipwayShippinMethod.carrier_id,
        #     "awb": ShipwayShippinMethod.awb,
        #     "order_id": ShipwayShippinMethod.order_id,
        #     "first_name": ShipwayShippinMethod.first_name,
        #     "last_name": ShipwayShippinMethod.last_name,
        #     "email": ShipwayShippinMethod.email,
        #     "phone": ShipwayShippinMethod.phone,
        #     "products": ShipwayShippinMethod.products,
        #     "company": ShipwayShippinMethod.company
        # }

        # place_order_url = "https://shipway.in/api/PushOrderData"
        # push_order_api = requests.post(place_order_url, headers=getHeaders(), data=json.dumps(values))
        # final_data = push_order_api.json()

        # if final_data['status'] == 'Success':
        #     Orders.objects.create(
        #         carrier_id = ShipwayShippinMethod.carrier_id,
        #         awb = ShipwayShippinMethod.awb,
        #         order_id = ShipwayShippinMethod.order_id,
        #         first_name = ShipwayShippinMethod.first_name,
        #         last_name = ShipwayShippinMethod.last_name,
        #         email = ShipwayShippinMethod.email,
        #         phone = ShipwayShippinMethod.phone,
        #         product_desc = ShipwayShippinMethod.products,
        #         company = ShipwayShippinMethod.company
        #     )
        #     return Response({"status": 'success', 'message': 'Order has been created successfully'}, status=status.HTTP_200_OK) 

        # if final_data['status'] == "Failed":
        #     return Response({"status": final_data['status'], 'message': final_data['message']}, status=status.HTTP_200_OK)
    
    @csrf_exempt
    @api_view(('POST',))
    def print_waybill_label(self):
        print("Waybill printed")
        return Response({"status": "Success"}, status=status.HTTP_200_OK)


    @csrf_exempt
    @api_view(('POST',))
    def get_status(self):
        print("Get status")
        return Response({"status": "Success"}, status=status.HTTP_200_OK)

