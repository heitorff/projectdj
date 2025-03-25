from django.shortcuts import render
from django.http import HttpResponse

def home(request, *args, **kwargs):
    return render(request, 'recipes/home.html', {})

def contato(request, *args, **kwargs):
    return HttpResponse('Contato')

def sobre(request, *args, **kwargs):
    return HttpResponse('Sobre')