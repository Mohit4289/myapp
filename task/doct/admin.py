from django.contrib import admin
from .models import Sign
from django.contrib.auth import get_user_model


@admin.register(Sign)
class Sign(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username')
    search_fields = ('first_name', 'last_name', 'email', 'username')
    list_filter = ('city', 'state', 'pincode')
