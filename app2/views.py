from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def virat(request):
    return HttpResponse('virat is the run machine')

def gayle(request):
    return HttpResponse('gayle is the monster in the cricket')