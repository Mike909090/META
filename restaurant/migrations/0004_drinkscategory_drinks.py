# Generated by Django 4.1.5 on 2023-10-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='restaurant.drinkscategory')),
            ],
        ),
    ]
