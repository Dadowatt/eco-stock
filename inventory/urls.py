from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = router.urls

