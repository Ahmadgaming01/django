# Generated by Django 4.2.1 on 2023-06-10 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pro_productImage', models.ImageField(upload_to='ImageProduct/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pro_Name', models.CharField(max_length=50)),
                ('Pro_Descrebition', models.TextField(max_length=15000)),
                ('Pro_Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Pro_Cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Pro_crate_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Pro_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productimage')),
            ],
        ),
    ]