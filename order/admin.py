from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['id', 'status', 'description']
    ordering = ['id']
