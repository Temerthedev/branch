# Generated by Django 4.2.7 on 2023-12-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0024_alter_warehouseproduct_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproduct',
            name='status',
            field=models.CharField(choices=[('sold', 'Sold'), ('available', 'Available')], default='available', max_length=40),
        ),
    ]