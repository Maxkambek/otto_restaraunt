from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.request.GET.get('id')
        queryset = Product.objects.all()
        if pk:
            queryset = Product.objects.filter(parentGroup=pk)
        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
