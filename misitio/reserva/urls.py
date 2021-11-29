from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("inicio", views.inicio, name="inicio"),
    path("login", views.login, name="login"),
    path("registrarse", views.registrarse, name="registrarse"),
    path("clientes", views.clientes, name="clientes"),
]