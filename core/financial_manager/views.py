from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'financial_manager/home.html')

def cash_flow(request):
    return render(request, 'financial_manager/cash_flow.html')

def investimentos(request):
    return render(request, 'financial_manager/investimentos.html')

def settings(request):
    return render(request, 'financial_manager/settings.html')
