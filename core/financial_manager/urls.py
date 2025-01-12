from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cash_flow/', views.cash_flow, name='cash_flow'),
    path('investimentos/', views.investimentos, name='investimentos'),
    path('settings/', views.settings, name='settings'),
]
