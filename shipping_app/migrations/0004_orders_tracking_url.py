# Generated by Django 4.1.3 on 2022-11-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_app', '0003_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='tracking_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]