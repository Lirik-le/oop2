from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


class DesLogoutView(LogoutView):
    template_name = 'registration/logout.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
