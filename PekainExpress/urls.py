from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('show/<titre>', views.show, name="show"),
    path('random/', views.random, name= "random")
]