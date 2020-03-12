from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    #user form is already given by django
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
