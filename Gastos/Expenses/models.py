from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Expenses(models.Model):
    CATEGORY_CHOICES = [
        ('Comida', 'Comida'),
        ('Transporte', 'Transporte'),
        ('Entretenimiento', 'Entretenimiento'),
        ('Salud', 'Salud'),
        ('Otro', 'Otro'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses') #relacion con el usuario
    title = models.CharField(max_length=100) #titulo de del gasto
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date_created = models.DateField(default=date.today)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    #Si el usuario se ellimina se eliminas todos sus gastos relacionados con ese usuario

    #related_name="expenses" permite hacer user.expenses.all() para obtener todos los gastos de un usuario

    def __str__(self):
        return f"{self.title} - {self.amount}" #esto define como se muestra el objeto en el admin o en la shell de django, es solo para que sea mas legible y entendible