from django.db import models
from django.urls import reverse_lazy

from product.models import Product

STATUS_CHOICES = [
    [1, "created"],
    [2, "in process"],
    [3, 'complete'],

]


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_date = models.DateField(auto_created=True, auto_now=True)
    updated_date = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, default="description")

    def __repr__(self):
        return f"Order ('{self.id}')"

    def __str__(self):
        return f"{self.id}-{self.description}-{self.status} "

    def get_absolute_url(self):
        return reverse_lazy("order-detail", kwargs={"pk": self.id})
