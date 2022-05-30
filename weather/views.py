from re import A
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Weather
import requests

def search(request):
    city =  request.POST.get('city') #request.POST['title'] # throws an exception if value does not exist 
    if city:
        data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=5a008aceca448cf6719f172c9ecdeeff').json()
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