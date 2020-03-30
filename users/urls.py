from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='blog-register'), #views.home is functio created in views.py
    path('',views.profile, name='user-profile'),
]