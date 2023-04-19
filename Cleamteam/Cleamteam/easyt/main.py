from django.contrib import admin
from django.urls import path
from teamer import views

urlpatterns = [
    path('', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('teller/', views.teller, name='teller'),
]