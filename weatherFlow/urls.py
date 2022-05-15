#views.py file which holds all the urls
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]