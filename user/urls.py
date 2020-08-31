from . import views
from django.urls import path
from django.contrib.auth.views import  LoginView,LogoutView
app_name = 'user'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]