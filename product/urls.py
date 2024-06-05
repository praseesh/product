"""
URL configuration for product project.

The `urlpatterns` list routes URLs to views. For more information please see:
views

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path ('', include('product1.urls'))
]
