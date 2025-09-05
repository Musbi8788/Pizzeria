from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas/', views.my_pizzas, name='my_pizzas'),
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),

]