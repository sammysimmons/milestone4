from django.shortcuts import render

# Create your views here.
def portfolio(request):
    """ A view to return the portfolio index"""
    return render(request, 'portfolio/portfolio.html')