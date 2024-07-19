from django.urls import path
from .views import index, autocomplete, history, register

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('history/', history, name='history'),
]
