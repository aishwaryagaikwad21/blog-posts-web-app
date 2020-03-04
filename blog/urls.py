#application level urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-name'), #views.home is functio created in views.py
    path('about/', views.about, name='blog-about'),
    path('help/', views.help, name='blog-help'),
]

