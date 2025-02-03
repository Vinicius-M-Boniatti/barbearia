from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.tela_inicial_view, name='tela_inicial'),
]
