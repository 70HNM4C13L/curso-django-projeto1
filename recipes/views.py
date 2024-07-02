#from django.shortcuts import render
from django.http import HttpResponse

def _test(request):
    return HttpResponse("About informations....")

def _home(request):
    return HttpResponse("Home PAge.")

def _contacts(request):
    return HttpResponse('Our contacts here...')