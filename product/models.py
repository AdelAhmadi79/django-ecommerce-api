from django.db import models
from django.contrib.auth.models import User
class Category(models.TextChoices):
        ELECTRONIC = "Electronic"
        LAPTOP = "Laptop"
        ART = "Art"
        FOOD = "Food"
        HOME = "Home"
        KITCHEN = "Kitchen"
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, default="" , blank=False)
    description = models.TextField(max_length=1000, default="" , blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    brand = models.CharField(max_length=200, default="" , blank=False)
    category = models.CharField(max_length=30,choices= Category.choices)
    rating = models.DecimalField(max_digits=3, decimal_places=2 , default=0)
    stock = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)