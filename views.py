from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def new(request):
    return HttpResponse('New products')


#so from django.shortcuts we're importing render function.Here django is a package and shortcut is module
#and render is a function
#Here httpResponse is a class with this class we can create an http response to return to the client
#or the browser

# Create your views here.
#All are view functions take parameters
