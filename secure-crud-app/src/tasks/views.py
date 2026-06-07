from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from tasks.forms import SecureRegisterForm, TaskForm
from tasks.models import Task

# ==========================================
# 1. USER REGISTRATION & LOGIN
# ==========================================
def register_view(request):
    if request.method == 'POST':
        form = SecureRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            messages.success(request, "Pendaftaran akaun berjaya!")
            return redirect('login')
    else:
        form = SecureRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# ==========================================
# 2. LOG OUT (LOG KELUAR SELAMAT - OWASP A2)
# ==========================================
def logout_view(request):
    logout(request)
    messages.success(request, "Anda telah selamat log keluar.")
    return redirect('login')

# ==========================================
# 3. USER PROFILE PAGE (Muka Surat 4, Point 4)
# ==========================================
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'tasks/profile.html')

# ==========================================
# 4. CRUD MODULES (SECURED WITH ACCESS CONTROL)
# ==========================================

# READ & CREATE
@login_required(login_url='login')
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Tugasan berjaya ditambah!")
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/dashboard.html', {'tasks': tasks, 'form': form})

# UPDATE
@login_required(login_url='login')
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tugasan berjaya dikemaskini!")
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

# DELETE
@login_required(login_url='login')
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Tugasan berjaya dipadam!")
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# ==========================================
# 5. AUDIT LOG PAGE (Khusus Untuk Admin - Muka Surat 4)
# ==========================================
@login_required(login_url='login')
def audit_log_view(request):
    # KAWALAN KESELAMATAN: Sekat kalau user bukan Superuser/Admin (RBAC)
    if not request.user.is_superuser:
        raise PermissionDenied  # Hantar ralat 403 Forbidden secara selamat
        
    # Ambil semua data tugasan daripada semua user untuk tujuan pemantauan admin
    logs = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/audit_log.html', {'logs': logs})