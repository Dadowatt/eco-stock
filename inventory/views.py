from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Warehouse, Product
from .serializers import WarehouseSerializer, ProductSerializer

class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

