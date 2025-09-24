from django.contrib import admin
from .models import Expenses

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'user', 'date_created')
    list_filter = ('category', 'user', 'date_created')
    search_fields = ('title',)
