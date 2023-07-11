from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "role")
    list_filter = ()
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
