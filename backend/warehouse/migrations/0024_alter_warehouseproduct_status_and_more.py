# Generated by Django 4.2.7 on 2023-12-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0023_warehouseproduct_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproduct',
            name='status',
            field=models.CharField(choices=[('sold', 'Sold'), ('available', 'Available')], default='available', max_length=40),
        ),
        migrations.AlterField(
            model_name='warehouseproduct',
            name='total_price',
            field=models.FloatField(blank=True),
        ),
    ]
