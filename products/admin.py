from django.contrib import admin

from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "available", "create_at"]
    search_fields = ["name", "price"]


admin.site.register(Product, ProductAdmin)
