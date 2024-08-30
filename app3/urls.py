from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index),
    path('pagina3/', views.pagina3)
]
