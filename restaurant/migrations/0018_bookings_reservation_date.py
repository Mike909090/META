# Generated by Django 4.1.5 on 2023-12-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_remove_orderitem_unit_price_alter_cart_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='reservation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
