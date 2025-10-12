from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
]