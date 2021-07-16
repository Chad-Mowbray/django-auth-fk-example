from django.db import models
from django.contrib.auth.models import AbstractUser


class MySiteUser(AbstractUser):
    class Meta:
        verbose_name = "MySiteUser"
        verbose_name_plural = "MySiteUsers"


class Profile(models.Model):
    my_user = models.OneToOneField(MySiteUser, on_delete=models.CASCADE)
    fav_color = models.CharField(max_length=100)