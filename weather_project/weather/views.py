import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SearchHistory
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def get_weather(city):
    url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "hourly": [
                {
                    "time": datetime.strptime(time, "%Y-%m-%dT%H:%M"),
                    "temperature": temp
                }
                for time, temp in zip(data["hourly"]["time"],
                                      data["hourly"]["temperature_2m"])
            ]
        }
    return None


def index(request):
    weather_data = None
    city = None
    if 'city' in request.GET:
        city = request.GET['city']
        weather_data = get_weather(city)
        if request.user.is_authenticated:
            SearchHistory.objects.create(user=request.user, city=city)
    return render(request, 'weather/index.html',
                  {'city': city,
                   'weather_data': weather_data})


def autocomplete(request):
    if 'term' in request.GET:
        cities = ["London", "Los Angeles", "Paris", "Berlin"]
        suggestions = [city for city in cities if city.lower().startswith(request.GET['term'].lower())]
        return JsonResponse(suggestions, safe=False)


@login_required
def history(request):
    search_history = SearchHistory.objects.filter(user=request.user)
    return render(request, 'weather/history.html',
                  {'search_history': search_history})
