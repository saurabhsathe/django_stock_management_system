from django.contrib import admin
from .form import StockCreateForm
# Register your models here.
from .models import Stock

class adminForm(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
   

admin.site.register(Stock,adminForm)