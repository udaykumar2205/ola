from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def auto(request):
    return HttpResponse('<h1>auto is a 3 wheeler...This is the mind of pure vegetarians</h1>')