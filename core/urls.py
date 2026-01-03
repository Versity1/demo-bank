from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('accounts/detail/', views.account_detail, name='account_detail'),
    path('cards/', views.card_mgt, name='card_mgt'),
    path('transactions/', views.transaction_history, name='transaction_history'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('loans/', views.loan_mgt, name='loan_mgt'),
    path('deposit-withdrawal/', views.deposit_withdrawal, name='deposit_withdrawal'),
    path('exchange/', views.currency_exchange, name='currency_exchange'),
]
