from django.contrib import admin
from django.urls import path

from server.product.views import ProductListCreateAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/products", ProductListCreateAPIView.as_view()),
    path("api/v1/products/<int:product_id>", ProductRetrieveAPIView.as_view()),
]
