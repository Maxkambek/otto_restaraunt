from django.urls import path
from .views import API

urlpatterns = [
    path('alo/', API.as_view())
]
