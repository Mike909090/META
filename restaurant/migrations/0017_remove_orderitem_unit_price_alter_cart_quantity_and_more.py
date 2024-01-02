# Generated by Django 4.1.5 on 2023-12-18 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_category_order_remove_menuitem_inventory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='unit_price',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='restaurant.order'),
        ),
    ]
