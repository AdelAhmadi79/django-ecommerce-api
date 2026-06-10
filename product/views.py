from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
@api_view (['GET'])
def get_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({"products": serializer.data})

@api_view(['GET'])
def get_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"product": serializer.data})