from django.shortcuts import render
from phone import models
# Create your views here.
def index(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', locals())

def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        # images = 
    except:
        pass
    return render(request, 'detail.html', locals())