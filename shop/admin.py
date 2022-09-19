from django.contrib import admin
from .models import Item, Category, Order

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)