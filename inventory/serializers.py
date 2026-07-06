from rest_framework import serializers
from .models import Warehouse, Product


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ("id", "name", "location", "capacity")


class ProductSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)

    warehouse_id = serializers.PrimaryKeyRelatedField(
        queryset=Warehouse.objects.all(),
        source="warehouse",
        write_only=True,
    )
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "quantity",
            "expiration_date",
            "status",
            "warehouse",
            "warehouse_id",
        )