# Generated by Django 4.2.7 on 2024-02-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_remove_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
