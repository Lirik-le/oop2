from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', DesLogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('profile', profile, name='profile'),
    path('register', RegisterView.as_view(), name='register',)
]
