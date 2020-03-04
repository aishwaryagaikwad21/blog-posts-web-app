from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html') #when user goes to home blog page


def about(request):
    return render(request, 'about.html')

def help(request):
    return HttpResponse('<h1>Thanks</h1>')