from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
# Create your views here.

def base(request):
    return render(request,"craigslist/base.html")

def new_search(request):
    search_query = request.POST.get('new_search_text')
    context = {
        "search_query" : search_query,
    }
    return render(request,"craigslist/new_search.html",context)
