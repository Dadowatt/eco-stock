from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def move(self, request, pk=None):
        product = self.get_object()
        new_warehouse_id = request.data.get("warehouse")
        if not new_warehouse_id:
            return Response(
                {"error": "Le champ 'warehouse' est requis."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        new_warehouse = get_object_or_404(
            Warehouse,
            pk=new_warehouse_id
        )
        if product.status == "expired":
            return Response(
                {
                    "error": "Impossible de déplacer un produit périmé."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        product.warehouse = new_warehouse
        product.save()
        return Response(
            {
                "message": "Produit déplacé avec succès.",
                "warehouse": product.warehouse.id,
            },
            status=status.HTTP_200_OK,
        )
