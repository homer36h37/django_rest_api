from django.db import models

# Create your models here.

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    full_name = models.CharField(verbose_name=_("ФИО"), max_length=300)
    birthdate = models.DateTimeField(verbose_name=_("Дата рождения"))

    def __str__(self):
        return f"Сотрудник: {self.full_name}"

class Client(models.Model):
    full_name = models.CharField(verbose_name=_("ФИО"), max_length=300)
    birthdate = models.DateTimeField(verbose_name=_("Дата рождения"))

    def __str__(self):
        return f"Покупатель: {self.full_name}"

class Product(models.Model):
    name = models.CharField(verbose_name=_("Наименование"), max_length=300)
    quantity = models.IntegerField(verbose_name=_("В наличии"))
    price = models.DecimalField(decimal_places=2, max_digits=2, verbose_name=_("Цена"))


    def __str__(self):
        return f"Продукт: {self.name}"

class Order(models.Model):
    сlient = models.CharField(verbose_name=_("Клиент"), max_length=300)
    product = models.ManyToManyField('Product', verbose_name=_("Товары"))
    employee = models.CharField(verbose_name=_("Сотрудник"), max_length=300)
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.pk} Дата: {self.created_date}"


class Statistic(models.Model):
    full_name_employee = models.CharField(verbose_name=_("ФИО"), max_length=300)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_("id сотрудника"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_("id клиента"))
    full_name_client = models.CharField(verbose_name=_("ФИО"), max_length=300)

    quantity_clients = models.IntegerField(verbose_name=_("Количество клиентов"))
    quantity_products = models.IntegerField(verbose_name=_("Количество товаров"))
    total_price = models.IntegerField(verbose_name=_("Сумма продаж"))
    created_date = models.DateTimeField()
