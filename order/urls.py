from django.urls import path
from django.views.generic import DeleteView

from order.views import order_list, OrderCreateView, OrderDetailView, UpdateView

urlpatterns = [
    path("order/", order_list, name="order-list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("<int:pk>/update/", UpdateView.as_view(), name="order-update"),
    path("<int:pk>/delete/", DeleteView.as_view(), name="order-delete"),
]