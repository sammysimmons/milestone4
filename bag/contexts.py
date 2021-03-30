from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_name, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_name)
        total = product.price
        bag_items.append({
            'item_name' : item_name,
            'product' : product,
        })

    if total:
        delivery = 0
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }


    return context