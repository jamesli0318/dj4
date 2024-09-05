from django.shortcuts import render
from django.http import HttpResponse, Http404
from ch4_app.models import Product
import random
# Create your views here.
def about (request):
    quotes = ['To be or not to be is a question.',
            'A dog jumps over a lazy fox.',
            'Knowledge is power.']
    quote = random.choice(quotes)

    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all()
    render(request, 'list.html', locals())
    
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('Not found item.')
    
    return render(request, 'disp.html', locals())