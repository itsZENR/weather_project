from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    date_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} searched by {self.user.username}"


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
