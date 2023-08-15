from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rooms/', include('chatapp.urls')),
]
