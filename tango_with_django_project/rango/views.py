from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {
        'aboldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {
        'aboldmessage': 'This tutorial has been put together by Tin-Trung Pham.'
    }
    return render(request, 'rango/about.html', context=context_dict)