# Generated by Django 4.0.3 on 2023-02-21 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_customer_order_customer1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer1',
            new_name='customer',
        ),
    ]