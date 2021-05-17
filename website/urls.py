from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('sme-finance/', views.sme_finance, name='sme-finance'),
    path('payroll-based/', views.payroll_based, name='payroll-based'),
    path('retail-based/', views.retail_based, name='retail-based'),
    path('consumer-based/', views.consumer_based, name='consumer-based'),
    path('purchase-order/', views.purchase_order, name='purchase-order'),
    path('about/', views.about, name='about'),
    path('calculator/', views.calculator, name='calculator'),
    path('contact/', views.contact, name='contact'),
    path('pdf-file/', views.pdf_view, name='pdf-file'),
    path('news/', views.news, name='news'),
    path('news_detail/<public_id>', views.news_details, name='news_detail'),
]