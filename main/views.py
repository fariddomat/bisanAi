from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import SearchForm,AddMapForm
from .search import  searchFunction, storeFunction




def home(response):
    return render(response,'main/home.html')

def searchMap(response):
    data=""
    if response.method=="POST":
        search_form=SearchForm(response.POST)
        if search_form.is_valid():
            data = searchFunction(search_form.cleaned_data["source"],search_form.cleaned_data["destination"])
         
    else:
        search_form=SearchForm()
    return render(response,'main/searchMap.html', {"search_form":search_form, "data":data})

def addMap(response):
    data=""
    if response.method=="POST":
        add_map_form=AddMapForm(response.POST)
        if add_map_form.is_valid():
            data = storeFunction(add_map_form.cleaned_data["romania_Cities"],add_map_form.cleaned_data["heuristic_Value"])
              
    else:
        add_map_form=AddMapForm()
    return render(response,'main/map.html', {"add_map_form":add_map_form,"data":data})
