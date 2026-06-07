from django.contrib import admin
from tasks.models import Task

# Mendaftarkan model Task supaya Admin boleh pantau semua aktiviti CRUD pengguna
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at') # Kolum yang dipapar dalam admin panel
    list_filter = ('is_completed', 'created_at', 'user')          # Menu tapisan di sebelah kanan
    search_fields = ('title', 'description')                      # Kotak carian pantas