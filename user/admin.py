from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'email', 'city', 'country', 'is_superuser', 'is_staff', 'is_active')
    list_display_links = ('username', 'first_name', 'last_name')
    list_filter = ('city', 'country',)
    search_fields = ['username', 'email', 'last_name']
    search_help_text = 'Vous pouvez rechercher par username, email ou nom'


admin.site.register(User, UserAdmin)
