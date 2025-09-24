from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expenses
from .serializers import ExpensesSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class ExpensesListCreateView(APIView): #api view nos permite definir manualmente que hacer en cada metodo
    permission_classes = [IsAuthenticated] #solo usuarios autenticados pueden acceder a esta vista
    def get(self, request):
        expenses = Expenses.objects.filter(user=request.user) #Obtenemos todos los gastos de la bd
        serializer = ExpensesSerializer(expenses, many=True) #los convertimos a json, many true porque son varios objetos
        return Response(serializer.data) #retorna los datos en la respuesta, manda los datos al frontend como json
    

    def post(self, request):
        serializer = ExpensesSerializer(data=request.data) #convierte el json recibido a un objeto de python
        if serializer.is_valid(): #valida que los datos sean correctos
            serializer.save(user=request.user) #guarda el nuevo gasto en la bd
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExpenseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk, user=request.user)
        serializer = ExpensesSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk, user=request.user)
        serializer = ExpensesSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk, user=request.user)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)