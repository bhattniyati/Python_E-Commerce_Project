# Generated by Django 5.0.1 on 2024-04-25 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_remove_order_created_at_remove_order_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="net_price",
        ),
    ]
