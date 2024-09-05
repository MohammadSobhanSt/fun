from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.accounts, name='accounts'),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout, name='logout'),
]