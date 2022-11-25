from django.db import models

# Create your models here.


class CouriersCompany(models.Model):
    company_id = models.IntegerField()
    courier_name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.courier_name


STATUSCHOICES = (
    ("DEL", "Delivered"),
    ("INT", "In Transit"),
    ("UND", "Undelivered"),
    ("RTO", "RTO"),
    ("RTD", "RTO Delivered"),
    ("CAN", "Cancelled"),
    ("SCH", "Shipment Booked"),
    ("PKP", "Picked Up"),
    ("OOD", "Out for Delivery"),
    ("NWI", "Network Issue"),
    ("DNB", "Delivery Next Day"),
    ("NFI", "Not Found/Incorrect"),
    ("ODA", "Out of Delivery Area"),
    ("OTH", "Others"),
    ("SMD", "Delivery Delayed"),
    ("CRTA", "Customer Refused"),
    ("CNA", "Consignee Unavailable"),
    ("DEX", "Delivery Exception"),
    ("DRE", "Delivery Rescheduled"),
    ("PNR", "COD Payment Not Ready"),
    ("LOST", "Shipment Lost"),
    ("PKF", "Pick up Failed"),
    ("PCAN", "Pick up Cancelled"),
    ("FDR", "Future Delivery Requested"),
    ("22", "Address Incorrect"),
    ("23", "Delivery Attempted"),
    ("24", "Pending - Undelivered"),
    ("25", "Delivery Attempted-Premises Closed"),
)


class Orders(models.Model):
    carrier_id = models.IntegerField()
    awb = models.IntegerField(unique=True)
    order_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    product_desc = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUSCHOICES, default="OTH")
    tracking_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.awb)