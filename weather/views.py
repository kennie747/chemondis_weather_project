from re import A
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Weather
import requests

def search(request):
    # return HttpResponse('Hello there')

    city =  request.POST.get('city') #request.POST['title'] # throws an exception if value does not exist 
    
    if city:
        data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=5a008aceca448cf6719f172c9ecdeeff').json()
        return render(request, 'weather/weather.html', {'weather':data, 'input':city})

    else:
        return render(request, 'weather/weather.html')


    # data = requests.get('http://api.openweathermap.org/data/2.5/weather?q=london,uk&APPID=5a008aceca448cf6719f172c9ecdeeff').json()
    # return render(request, 'weather/weather.html', {'weather':data})

def home(request):
    return render(request, 'weather/weather.html')
    # return HttpResponse("Home Page")
def weather(request):
    return render(request, 'weather/weather.html')
    # return HttpResponse("Home Page")