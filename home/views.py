from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def index(request):
    """ A view to show 3 standard services on the homepage to checkout """
    product1 = get_object_or_404(klass=Product, pk=2)
    product2 = get_object_or_404(klass=Product, pk=4)
    product3 = get_object_or_404(klass=Product, pk=1)


    context = {
        'logoandbrand': product1,
        'landingpage': product3,
        'appdesign': product2,
    }   

    return render(request, 'home/index.html', context)