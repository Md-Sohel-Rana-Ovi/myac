from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from math import ceil

# Create your views here.


def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allprods=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allprods':allprods}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    print("sohel")
    return HttpResponse("We are at checkout")
