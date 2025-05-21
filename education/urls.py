from django.urls import path
from . import views

urlpatterns = [
    path('', views.program_form, name='program_form'),
    path('data/', views.data_list, name='data_list'),
    path('stats/', views.statistics, name='stats'),
]