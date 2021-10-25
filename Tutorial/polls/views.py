from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a Django App")
# Create your views here.
def trialView(request):
    return HttpResponse("This is a Trial View")

