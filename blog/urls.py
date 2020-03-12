#application level urls
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='blog-home'), #views.home is functio created in views.py
    path('about/', views.about, name='blog-about'),
    path('help/', views.help, name='blog-help'),
    path('base/', views.base,name="blog-base")
]

