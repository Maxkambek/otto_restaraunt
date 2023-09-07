from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view()),
    path('product/', views.ProductListAPIView.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view()),
]
