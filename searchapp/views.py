from django.shortcuts import render
from store.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
         query=request.GET.get('q')
         products = Product.objects.all().filter(Q(name__contians=query))
    return render(request,'search.html',{'query':query,'products':products})
# products=None
# query=None
# if 'q' in request.GET:
#      query=request.GET.get('q')
# products = Product.objects.filter(Q(name__contians=query))