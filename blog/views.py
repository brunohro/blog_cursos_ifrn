from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def ads(request):
    return render(request, 'blog/ads.html')

def agro_industria(request):
    return render(request, 'blog/agro_industria.html')

def alimentos(request):
    return render(request, 'blog/alimentos.html')

def apicultura(request):
    return render(request, 'blog/apicultura.html')

def informatica(request):
    return render(request, 'blog/informatica.html')

def quimica(request):
    return render(request, 'blog/quimica.html')