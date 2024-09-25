from django.urls import path
from .views import CreateOrderProductView, MyOrderView

urlpatterns = [
    path("mi_orden/", MyOrderView.as_view(), name="my_order"),
    path("agregar_producto", CreateOrderProductView.as_view(), name="add_product"),
]
