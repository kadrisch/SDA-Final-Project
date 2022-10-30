from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    content = 'Hello world! I am learning django!'

    return HttpResponse(content)
