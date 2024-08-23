from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index),
    path('pagina2/', views.presentacion)
]
