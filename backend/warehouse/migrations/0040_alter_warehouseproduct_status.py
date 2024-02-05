# Generated by Django 4.2.7 on 2024-01-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0039_alter_warehouseproduct_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproduct',
            name='status',
            field=models.CharField(choices=[('sold', 'Sold'), ('available', 'Available')], default='available', max_length=40),
        ),
    ]