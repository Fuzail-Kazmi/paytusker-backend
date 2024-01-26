# Generated by Django 4.2.3 on 2024-01-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_cartitem_qty_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('001', 'Order Pending'), ('004', 'Shipping'), ('002', 'Order Confirmed'), ('005', 'Delivered'), ('003', 'In Process')], max_length=999, null=True),
        ),
    ]
