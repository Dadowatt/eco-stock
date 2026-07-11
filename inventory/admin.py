from django.contrib import admin

from .models import Warehouse, Product

from django.db.models import Count

@admin.register(Warehouse)
class WarehousAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "capacity", "total_products",)
    search_fields = ("name", "location")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            product_count=Count("products")
        )

    def total_products(self, obj):
        return obj.product_count

    total_products.short_description = "Nombre de produits"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "status", "expiration_date", "warehouse",)
    list_filter = ("status", "warehouse")
    search_fields = ("name",)