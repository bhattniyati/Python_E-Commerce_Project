# Generated by Django 5.0.1 on 2024-04-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_remove_cart_net_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="payment_id",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
