from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from intsureview_be.apps.api.serializers import (
    GroupSerializer,
    PizzaSerializer,
    UserSerializer,
)
from rest_framework import permissions, viewsets

from .forms import PizzaForm

# Create your views here.
  


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

  
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = PizzaForm.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PizzaSerializer
    
    
    def get(self, request):
        detail = [ {"toppings": detail.toppings, 'extra_cheese': detail.extra_cheese, 'date': detail.date, 'time': detail.time, 'extra_instructions': detail.extra_instructions} 
        for detail in PizzaForm.objects.all()]
        print(detail)
        return HttpResponseRedirect(detail)

    def get_form(request):
        if request.method == "GET":
            form = PizzaForm(request.GET)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                print('valid')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PizzaForm()

        return render(request, "pizzaorder.html", {"form": form})



