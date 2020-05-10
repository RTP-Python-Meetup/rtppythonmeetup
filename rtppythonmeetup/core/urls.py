from django.contrib import admin
from django.urls import include, path

from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
]
