# Generated by Django 5.0.1 on 2024-04-20 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_cart_net_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="razor_pay_order_id",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="razor_pay_payment_id",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="razor_pay_payment_signature",
        ),
        migrations.AlterField(
            model_name="cart",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("mobile", models.PositiveBigIntegerField()),
                (
                    "picture",
                    models.ImageField(
                        default="media/profile.jpg", upload_to="profilepicture"
                    ),
                ),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=15)),
                ("state", models.CharField(max_length=15)),
                ("pincode", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
    ]
