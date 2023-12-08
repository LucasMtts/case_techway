from django.urls import path
from page_app.views import index, contato, services

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('services/', services), #incluído caminho para a renderização da página "nossos serviços"
    path('contato/', contato),
]
