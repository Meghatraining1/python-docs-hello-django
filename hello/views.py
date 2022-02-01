from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Congratulations! You have successfully created your web apps!")
