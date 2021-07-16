from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import MySiteUserCreationForm
from .models import MySiteUser

class MySiteLoginView(LoginView):
    template_name = "accounts/login.html"

class MySiteLogoutView(LogoutView):
    template_name = "accounts/logout.html"

class MySiteUserSignup(CreateView):
    model = MySiteUser
    template_name = "accounts/signup.html"
    form_class = MySiteUserCreationForm
    success_url = '/accounts/login/'
