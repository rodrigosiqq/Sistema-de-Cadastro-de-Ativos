from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarEstacao/', views.registrarEstacao),
    path('deletarEstacao/<identificador>', views.deletarEstacao)
    
]
