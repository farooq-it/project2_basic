from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('MSD is captain cool')


def raina(request):
    return HttpResponse('raina  is the mr.ipl')