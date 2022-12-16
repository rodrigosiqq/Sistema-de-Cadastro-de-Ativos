from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarEstacao/', views.registrarEstacao),
    path('edicaoEstacao/<identificador>', views.edicaoEstacao),
    path('editarEstacao/<int:identificador>', views.editarEstacao),
    path('deletarEstacao/<identificador>', views.deletarEstacao)
    
    
]
