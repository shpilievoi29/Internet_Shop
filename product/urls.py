from django.urls import path

from product.views import ProductListView, review,  ProductDetailView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("review/", review, name="review"),
]