from django.urls import path
from .views import MySiteLoginView, MySiteLogoutView, MySiteUserSignup

urlpatterns = [
    path('login/', MySiteLoginView.as_view()),
    path('logout/', MySiteLogoutView.as_view()),
    path('signup/', MySiteUserSignup.as_view())
]