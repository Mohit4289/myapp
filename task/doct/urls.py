from django.urls import path
from doct import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign/', views.sign),
    path('login/', views.login, name='login'),
]