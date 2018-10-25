from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register

# Routes for html pages

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register)
]
