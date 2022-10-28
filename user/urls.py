from django.urls import path

from . import views

urlpatterns = [
    path('register_user/', views.register_user, name='register'),
    path('login_user/', views.login_user, name='login'),
]
