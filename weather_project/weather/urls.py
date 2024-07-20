from django.urls import path, include
from .views import index, autocomplete, history, register, city_search_count


api = [
    path('city-search-count/', city_search_count, name='city_search_count'),
]

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('history/', history, name='history'),
    path('api/', include(api)),
]
