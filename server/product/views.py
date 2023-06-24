from opentelemetry import trace
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from server.common.utils import get_products, get_product_by_id
from server.product.serializers import ProductSerializer

tracer = trace.get_tracer(__name__)


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        with tracer.start_as_current_span('get-products') as span:
            products = get_products()
            return Response(data=products, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        with tracer.start_as_current_span('create-products') as span:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)


class ProductRetrieveAPIView(RetrieveAPIView):
    def get(self, request, product_id, *args, **kwargs):
        with tracer.start_as_current_span("get-product-by-id") as span:
            product = get_product_by_id(product_id)
            if not product:
                raise ValidationError("Product not found")
            return Response(data=product, status=status.HTTP_200_OK)
