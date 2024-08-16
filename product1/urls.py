
from django.urls import path, include
from . import views

urlpatterns = [
    path ('',views.home, name = "home"),
    path('add/', views.add, name='add'),
    path('display/', views.display, name='display'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),

    path('accounts/login/', views.loginview, name = 'login'),
    path('logout/', views.logout,name='logout'),
    path('accounts/sign_up/', views.sign_up, name="signup"),
    path('reset/', views.Resethome,name='reset'),
    path('passwordreset/',views.resetPassword, name="passwordreset")
]