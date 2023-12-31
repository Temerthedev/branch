# Generated by Django 4.2.7 on 2023-12-19 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0004_company_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_company', to=settings.AUTH_USER_MODEL),
        ),
    ]
