# Generated by Django 4.0.3 on 2023-02-21 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer1',
        ),
    ]
