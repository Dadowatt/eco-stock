from django.contrib import admin

from .models import Warehouse, Product

@admin.register(Warehouse)
class WarehousAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "capacity")
    search_fields = ("name", "location")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "status", "expiration_date", "warehouse",)
    list_filter = ("status", "warehouse")
    search_fields = ("name",)