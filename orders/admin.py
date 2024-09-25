from django.contrib import admin
from orders.models import Order
from orders.models import OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["user", "is_active", "order_date"]
    search_fields = ["user", "order_date"]
    inlines = [
        OrderProductInlineAdmin,
    ]


admin.site.register(Order, OrderAdmin)
