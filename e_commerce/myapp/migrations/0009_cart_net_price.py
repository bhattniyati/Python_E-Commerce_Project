# Generated by Django 5.0.1 on 2024-03-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_cart_razor_pay_order_id_cart_razor_pay_payment_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="net_price",
            field=models.IntegerField(default=0),
        ),
    ]
