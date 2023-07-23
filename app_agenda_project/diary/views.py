from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("hola")

def profile(request):
    pass

def login(request):
    pass

def close_session(request):
    pass

def signup(request):
    pass

def create_task(request):
    pass

def delete_task(request):
    pass