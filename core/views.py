from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # HTMX redirect
            response = HttpResponse()
            response['HX-Redirect'] = resolve_url('dashboard')
            return response
    else:
        form = LoginForm()

    if request.htmx:
        return render(request, 'partials/auth_login.html', {'form': form})
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # HTMX redirect
            response = HttpResponse()
            response['HX-Redirect'] = resolve_url('dashboard')
            return response
    else:
        form = RegisterForm()

    if request.htmx:
        return render(request, 'partials/auth_register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def account_detail(request):
    return render(request, 'account-detail.html')

def card_mgt(request):
    return render(request, 'card-mgt.html')

def transaction_history(request):
    return render(request, 'transaction-history.html')

def transfer_funds(request):
    return render(request, 'transfer-funds.html')

def loan_mgt(request):
    return render(request, 'loan-mgt.html')

def deposit_withdrawal(request):
    return render(request, 'deposit-withdrawal.html')

def currency_exchange(request):
    return render(request, 'currency-exchange.html')
