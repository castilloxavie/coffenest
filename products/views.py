from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProducListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
