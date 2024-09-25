from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )
    create_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="creado el"
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.price} - {self.create_at}"
