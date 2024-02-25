
from django.urls import path, include
from . import views

urlpatterns = [
    path ('',views.home),
    path('add/', views.add, name='add'),
    path('display/', views.display, name='display'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),

]