from django.shortcuts import render
import numpy_financial as npf
from . models import *
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf

def homeview(request):
    # Done
    return render(request, 'index.html')

def sme_finance(request):
    # Done
    return render(request, 'sme_finance.html')

def payroll_based(request):
    # DOne
    return render(request, 'payroll_based.html')

def retail_based(request):
    # Done
    return render(request, 'retail_based.html')

def consumer_based(request):
    # Done
    return render(request, 'consumer_based.html')

def purchase_order(request):
    # Done
    return render(request, 'purchase_order.html')

def about(request):
    # Done
    return render(request, 'about.html')

def calculator(request):
    if request.method == 'GET':
        loanz=Loans.objects.all()
        context={'loanz' : loanz}
        return render(request, 'calculator.html' , context)
    elif request.method == 'POST':
        # months = 12
        months = request.POST.get('period')
        loan = request.POST.get('amount')
        interest_rate = request.POST.get('percentage')
        # interest_rate = 41
        interest = int(interest_rate) / 1200
        # loan = 5000
        amount = float((float(interest) * -float(loan) * pow((1 + float(interest)), int(months)) / (1 - pow((1 + float(interest)), int(months)))))
        
        topay = float(float(amount) * int(months))
        pe = float(interest/100)
        # inter = round(loan*pe/12,2)
        # principal = round(amount - inter,2)
        # balances = round(loan - principal,2)
        # interestz = round(topay - loan,2)
        # bal = round(topay - amount,2)
        # capbal = round(loan - principal,2)
        # amount = npf.pmt(41, 12, 5000)
        # payback = npf.pmt(0.41/12, 12*2, 5000)
        
        return JsonResponse({'monthly_installment': round(amount,2), 'loan':loan, 'topay':round(topay,2), 'months':months, 'interest': interest_rate})

def news(request):
    blog = News.objects.all().order_by('-date_created')
    paginator = Paginator(blog, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', context={'blog':page_obj})

def contact(request):
    return render(request, 'contact.html')

def pdf_view(request):
    data = {
            'today': 'Lelo', 
            'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'order_id': 1233434,
    }
    pdf = render_to_pdf('homepdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def news_details(request,public_id):
    if request.method == 'GET':
        loanz=News.objects.get(public_id=public_id)
        context={'loanz' : loanz}
        return render(request, 'news_details.html', context)