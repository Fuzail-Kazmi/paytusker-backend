# Generated by Django 4.2.3 on 2024-01-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_cartitem_cart_alter_cartitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('003', 'In Process'), ('005', 'Delivered'), ('004', 'Shipping'), ('001', 'Order Pending'), ('002', 'Order Confirmed')], max_length=999, null=True),
        ),
    ]
