import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
import re
from . import models

base_url = "https://losangeles.craigslist.org/search/sss?query={}"
base_image_url = "https://images.craigslist.org/{}_300x300.jpg"

def base(request):
    return render(request, "craigslist/base.html")


def new_search(request):
    final_postings = []
    search_query = request.POST.get('new_search_text')
    models.Search.objects.create(SearchField=search_query.title())
    final_url = base_url.format(quote_plus(search_query))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")
    result_content = soup.find_all('li', {"class": "result-row"})

    for post in result_content[:9]:
        result_title = post.find(class_='result-title').text
        result_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            result_price = post.find(class_='result-price').text
        else:
            result_price = "N/A"
        if post.find(class_='result-image').get('data-ids'):
            image_id = post.find(class_='result-image').get('data-ids').split(",")[0][2:]
            final_image_id = base_image_url.format(image_id)
        else:
            final_image_id = "https://cdni.pornpics.com/1280/5/179/58314356/58314356_008_4c77.jpg"
        final_postings.append((result_title,result_price,result_url,final_image_id))

    print(final_url)
    context = {
        'final_postings': final_postings,
        "search_query": search_query,
    }
    return render(request, "craigslist/new_search.html", context)
