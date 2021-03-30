from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """This will prevent people from manually accessing the URL by typing /checkout and render order form"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IanVEERPw2gVvEQXw4ZThIPP4Vlk8GFjyjmp6YaLV3z8EZQlLXTusKOTzjTdm62xgnwKzsAIlodt9aUNBReOA5L0030VCC1al',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)