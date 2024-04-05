from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"hello/index.html")
def omar(request):
    return HttpResponse("Hello Omar!")

def greet(request,name):
    return render(request,"hello/greet.html",{'name':name.capitalize()})
