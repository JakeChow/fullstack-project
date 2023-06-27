# Generated by Django 4.2.2 on 2023-06-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PizzaForm",
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
                ("toppings", models.CharField(max_length=100)),
                ("extra_cheese", models.BooleanField()),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("extra_instructions", models.CharField(max_length=100)),
            ],
        ),
    ]
