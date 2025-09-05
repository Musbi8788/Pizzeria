from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

def my_pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    contexts = {'pizzas': pizzas}
    return render(request, "pizzas/my_pizzas.html", contexts)

def pizza(request, pizza_id):
    """Show a signle pizza with it entries."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name') # topping_set is used because of the have topping model name
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, "pizzas/pizza.html", context)
