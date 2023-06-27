from django.db import models


class PizzaForm(models.Model):
    toppings = models.CharField(max_length=100)
    extra_cheese = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()
    extra_instructions = models.CharField(max_length=100)
