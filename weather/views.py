import json
from re import A
from async_timeout import timeout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Weather
import requests
from django.core.cache import cache
from django.http import JsonResponse
from weather import config
import aiohttp
import asyncio
from asgiref.sync import sync_to_async

def save_config(request):
    if request.POST.get('cache_duration'):
        config.cache_timeout = request.POST.get('cache_duration')
    print(f'cache_timeout set to:  {config.cache_timeout}')
    return render(request, 'weather/config.html',{'set_val':int(int(config.cache_timeout)/60)})

def configuration(request):
    return render(request, 'weather/config.html',{'set_val':int(int(config.cache_timeout)/60)})

async def search(request):
    city =  request.POST.get('city') #request.POST['title'] # throws an exception if value does not exist 
    if city:
        if cache.get(city):
            data = cache.get(city)
            # print('cached')
        else:    
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=5a008aceca448cf6719f172c9ecdeeff') as res:
                    data = await res.json()
                    # data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=5a008aceca448cf6719f172c9ecdeeff').json()
            cache.set(city, data, timeout = int(config.cache_timeout))
            # print('database')
        return render(request, 'weather/weather.html', {'weather':data, 'input':city})
    else:
        return render(request, 'weather/weather.html')


def home(request):
    return render(request, 'weather/weather.html')

def weather(request):
    return render(request, 'weather/weather.html')

# Custom Error Pages
def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})