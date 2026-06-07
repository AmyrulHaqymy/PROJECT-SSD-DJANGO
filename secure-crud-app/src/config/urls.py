from django.contrib import admin
from django.urls import path
from tasks.views import register_view, login_view, dashboard_view, task_update_view, task_delete_view, logout_view, profile_view, audit_log_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('task/update/<int:pk>/', task_update_view, name='task_update'),
    path('task/delete/<int:pk>/', task_delete_view, name='task_delete'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('audit-log/', audit_log_view, name='audit_log'), # Jalur Audit Log
]