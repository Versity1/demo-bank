from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'John Doe',
        'class': 'w-full bg-slate-50 dark:bg-background-dark border border-slate-200 dark:border-surface-border rounded-lg pl-10 pr-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all shadow-sm'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'name@example.com',
        'class': 'w-full bg-slate-50 dark:bg-background-dark border border-slate-200 dark:border-surface-border rounded-lg pl-10 pr-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all shadow-sm'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create a password',
        'class': 'w-full bg-slate-50 dark:bg-background-dark border border-slate-200 dark:border-surface-border rounded-lg pl-10 pr-10 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all shadow-sm'
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def save(self):
        fullname = self.cleaned_data.get('fullname')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Split fullname into first and last name
        names = fullname.split()
        first_name = names[0]
        last_name = " ".join(names[1:]) if len(names) > 1 else ""

        # Create user with email as username
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'name@example.com',
        'class': 'w-full bg-slate-50 dark:bg-background-dark border border-slate-200 dark:border-surface-border rounded-lg pl-10 pr-4 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all shadow-sm'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full bg-slate-50 dark:bg-background-dark border border-slate-200 dark:border-surface-border rounded-lg pl-10 pr-10 py-3 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all shadow-sm'
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            # Authenticate using email as username
            user = authenticate(username=email, password=password)
            if not user:
                raise ValidationError("Invalid email or password.")
            self.user = user
        return cleaned_data
        
    def get_user(self):
        return getattr(self, 'user', None)
