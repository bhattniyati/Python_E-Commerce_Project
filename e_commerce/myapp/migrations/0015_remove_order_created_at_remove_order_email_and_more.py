# Generated by Django 5.0.1 on 2024-04-20 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_remove_order_city_remove_order_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="order",
            name="email",
        ),
        migrations.RemoveField(
            model_name="order",
            name="firstname",
        ),
        migrations.RemoveField(
            model_name="order",
            name="lastname",
        ),
        migrations.RemoveField(
            model_name="order",
            name="mobile",
        ),
        migrations.RemoveField(
            model_name="order",
            name="updated_at",
        ),
    ]
