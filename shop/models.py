from django.db import models


class Manufacturer(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="Производитель",
    )
    name = models.CharField("Название товара", max_length=200)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    in_stock = models.BooleanField("В наличии", default=True)

    def __str__(self):
        return self.name
