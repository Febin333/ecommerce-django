# Generated by Django 4.0.3 on 2023-02-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_customer1_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
