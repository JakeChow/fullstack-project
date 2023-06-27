from django.contrib.auth.models import Group, User
from intsureview_be.apps.api.forms import PizzaForm
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaForm
        fields = ['toppings', 'extra_cheese', 'date', 'time', 'extra_instructions']