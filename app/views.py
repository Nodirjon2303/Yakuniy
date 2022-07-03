from django.shortcuts import render, redirect, HttpResponse
from .models import *
def bazaView(request, key):
    try:
        fan = Fanlar.objects.get(key=key)
        baza = Baza.objects.filter(fan=fan).last()
        return redirect(f"{baza.baza.url}")
    except :
        return HttpResponse("Not Found")

def homeView(request):
    bazalar = Baza.objects.all()

    return render(request, 'home.html', {"baza":bazalar})
