from django.db import models

# Create your models here.
class Pizza(models.Model):
    """An object to handle Pizza's"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Topping(models.Model):
    """A class managing to pazza's topping"""
    name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_name = models.CharField(max_length=100, default="pineapple")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self) -> str:
        return self.pizza_name
    
