from django.urls import path
from . import views

my_app = 'pizzas'
urlpatterns = [
    path('', views.index, name='index')
]