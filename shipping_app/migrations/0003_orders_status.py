# Generated by Django 4.1.3 on 2022-11-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_app', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('DEL', 'Delivered'), ('INT', 'In Transit'), ('UND', 'Undelivered'), ('RTO', 'RTO'), ('RTD', 'RTO Delivered'), ('CAN', 'Cancelled'), ('SCH', 'Shipment Booked'), ('PKP', 'Picked Up'), ('OOD', 'Out for Delivery'), ('NWI', 'Network Issue'), ('DNB', 'Delivery Next Day'), ('NFI', 'Not Found/Incorrect'), ('ODA', 'Out of Delivery Area'), ('OTH', 'Others'), ('SMD', 'Delivery Delayed'), ('CRTA', 'Customer Refused'), ('CNA', 'Consignee Unavailable'), ('DEX', 'Delivery Exception'), ('DRE', 'Delivery Rescheduled'), ('PNR', 'COD Payment Not Ready'), ('LOST', 'Shipment Lost'), ('PKF', 'Pick up Failed'), ('PCAN', 'Pick up Cancelled'), ('FDR', 'Future Delivery Requested'), ('22', 'Address Incorrect'), ('23', 'Delivery Attempted'), ('24', 'Pending - Undelivered'), ('25', 'Delivery Attempted-Premises Closed')], default='OTH', max_length=50),
        ),
    ]
