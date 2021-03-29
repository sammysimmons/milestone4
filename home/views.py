from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def index(request):
    """ A view to show 3 standard services on the homepage to checkout """
    product1 = get_object_or_404(Product, pk=2)
    print(product1.name)
    product2 = get_object_or_404(Product, pk=4)
    print(product2.name)
    product3 = get_object_or_404(Product, pk=1)
    print(product3.name)

    context = {
        'logoandbrand': product1,
        'landingpage': product3,
        'appdesign': product2,
    }   

    return render(request, 'home/index.html', context)
