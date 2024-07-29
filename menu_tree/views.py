from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def demo(request, current_uri):
    return render(request, 'menu_tree/demo.html', context = {'current_uri': current_uri,
                                                             'request': request})

def test(request):
    current_uri = 'test'
    return render(request, 'menu_tree/demo.html', context = {'current_uri': current_uri,'request': request})