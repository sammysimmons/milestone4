from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def index(request):

    product = get_object_or_404(Product, pk=2)
    print(product.name)

    context = {
        'logoandbrand': product,
    }   

    return render(request, 'home/index.html', context)

