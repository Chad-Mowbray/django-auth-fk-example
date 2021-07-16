from django.contrib.auth.forms import UserCreationForm
from accounts.models import MySiteUser

class MySiteUserCreationForm(UserCreationForm):
    class Meta:
        model = MySiteUser
        fields = ("username", "password1", "password2")
