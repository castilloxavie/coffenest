from .views import ProductFormView, ProductListView
from django.urls import path

urlpatterns = [
    path('producto/', ProductListView.as_view(), name='product_list'),
    path('agregar/', ProductFormView.as_view(),  name='add_product'),
]
