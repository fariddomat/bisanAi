from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("searchMap", views.searchMap, name="searchMap"),
    path("addMap", views.addMap, name="addMap"),
    
]
