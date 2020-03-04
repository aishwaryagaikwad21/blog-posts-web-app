from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
posts = [
    {
        'author':'abc',
        'title': 'Post 1',
        'content':'Machine Learing',
        'data_posted':'March 04,2020'
    },
    {
        'author':'xyz',
        'title': 'Post 2',
        'content':'Block Chain',
        'data_posted':'March 05,2020' 
    }
]

def home(request):
    content = {
        'posts':posts
    }

    return render(request, 'home.html',content) #when user goes to home blog page


def about(request):
    return render(request, 'about.html',{'title':'aishwarya'})

def help(request):
    return HttpResponse('<h1>Thanks</h1>')