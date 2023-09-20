from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'myapp/index.html', context)


def detail_prod(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'myapp/detail.html', context)

