from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from tasks.models import Task  # <-- Kita letak kat atas ni berserta nama app 'tasks'

# ==========================================
# 1. BORANG PENDAFTARAN USER (REGISTER)
# ==========================================
class SecureRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, help_text="Minima 8 karakter.")
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email wajib diisi.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email ini sudah pun berdaftar.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Kedua-dua password tidak sepadan!")
        return cleaned_data


# ==========================================
# 2. BORANG INPUT TUGASAN (CRUD TASK)
# ==========================================
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 8px;', 'placeholder': 'Tajuk tugasan...'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%; padding: 8px;', 'rows': 3, 'placeholder': 'Deskripsi...'}),
        }