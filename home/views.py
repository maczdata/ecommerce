from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render (request, 'home/home.html')

def about(request):
    return render (request, 'home/about.html')

def products(request):
    return render (request, 'home/products.html')

def productdetail(request):
    return render (request, 'home/productdetail.html')

def contact(request):
    return render (request, 'home/contact.html')