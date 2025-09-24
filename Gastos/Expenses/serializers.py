from rest_framework import serializers
from .models import Expenses

#Creamos una clase serializer para el modelo expenses, los serializer son como un traductor para traducir el lenguaje de python a json y de json a python
class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses #indicamos que use nuestro modelo Expenses
        fields = ['id', 'title', 'amount', 'category']  # Incluimos los campos que queremos serializar
        #si quisiereamoc todos los campos se haria con fields = '__all__'  # Incluimos todos los campos del modelo