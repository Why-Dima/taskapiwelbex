from django.contrib import admin
from django.urls import path, include
from .views import CargoAPICreate, CargoAPIView, CarAPIUpdate

urlpatterns = [
    path('list_cargo/', CargoAPICreate.as_view()),
    path('create_cargo/<int:pk>/', CargoAPICreate.as_view()),
    path('cargo/<int:pk>/', CargoAPIView.as_view()),
    path('car/<int:pk>/', CarAPIUpdate.as_view()),
]