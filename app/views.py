from django.shortcuts import render, redirect
from .models import *
def bazaView(request, key):
    fan = Fanlar.objects.get(key=key)
    baza = Baza.objects.filter(fan=fan).last()
    return redirect(f"{baza.baza.url}")
