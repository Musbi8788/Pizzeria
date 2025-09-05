from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

def pizzas(request):
    """Represent to displaying Pizzas avaible in the database"""
    pizzas = Pizza.objects.all()
    contexts = {'pizzas': pizzas}
    return render(request, "pizzas/pizzas.html", contexts)