from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('checkout', views.checkout, name='checkout'),
    path('thanks', views.thanks, name='thanks')
]