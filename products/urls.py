from .views import ProducListAPI, ProductFormView, ProductListView
from django.urls import path

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("api/", ProducListAPI.as_view(), name="product_list_api"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
]
