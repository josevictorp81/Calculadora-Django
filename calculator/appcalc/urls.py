from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instrucoes', views.instrucoes, name='instrucoes'),
    path('subimit', views.subimit, name='subimit'),
]