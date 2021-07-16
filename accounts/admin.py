from django.contrib import admin
from .models import Profile, MySiteUser
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    list_display = ("username", "is_staff")

admin.site.register(MySiteUser, MyUserAdmin)
admin.site.register(Profile)
