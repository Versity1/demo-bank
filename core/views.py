from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

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
