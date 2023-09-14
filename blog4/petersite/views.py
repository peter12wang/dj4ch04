from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
from petersite.models import Product

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項')
    return render(request,'disp.html',locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

# Create your views here.
def index(request):
    quotes = ['得著智慧的，愛惜生命；',
            '保守聰明的，必得好處。',
            '人心多有計謀；',
            '惟有耶和華的籌算才能立定.']
    quote = random.choice(quotes)
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html',locals())
