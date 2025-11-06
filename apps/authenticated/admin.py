from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username','__str__','email','bale_id','is_active','is_staff','is_superuser')
    list_editable = ('is_active','is_staff','is_superuser')
    list_display_links = ('username','__str__')
    readonly_fields = ("date_joined", "last_login")
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","password1","password2","email","bale_id"),
            },
        ),
    )
    fieldsets = (
        (_('important fields'), {
            'classes':('wide'),
            'fields': (
                "username","email","password",
                "first_name","last_name","bale_id"
            ),
        }),
        (_('advanced fields'), {
            'classes':('wide'),
            'fields': (
                "date_joined","last_login"
            ),
        }),
    )