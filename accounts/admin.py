from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'email', 'birthday', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birthday',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
