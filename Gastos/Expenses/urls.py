from django.urls import path
from .views import ExpensesListCreateView, ExpenseDetailView, RegisterView

urlpatterns = [
    path('expenses/', ExpensesListCreateView.as_view(), name='expenses-list-create'), #.as_view() convierte la clase en una vista que puede manejar solicitudes HTTP, en este caso GET y POST
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('register/', RegisterView.as_view(), name='register'),
] #<int:pk> es un parametro que indica que se espera un entero que sera la clave primaria del gasto que queremos ver, actualizar o eliminar