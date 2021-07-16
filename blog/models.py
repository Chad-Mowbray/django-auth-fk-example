from django.db import models
from accounts.models import MySiteUser


class Post(models.Model):
    author = models.ForeignKey(MySiteUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    nth_post = models.IntegerField()

    def __str__(self):
        return self.title

