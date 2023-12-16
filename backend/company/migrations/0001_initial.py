# Generated by Django 4.2.7 on 2023-12-16 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('canteen', 'Canteen'), ('cafe', 'Cafe'), ('coffee_shop', 'Coffee Shop')], max_length=50)),
                ('company_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('barcode', models.CharField(max_length=255)),
                ('product_code', models.CharField(max_length=255)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='company.catalog')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='company.company')),
            ],
        ),
        migrations.AddField(
            model_name='catalog',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to='company.company'),
        ),
    ]