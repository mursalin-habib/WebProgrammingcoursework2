from django.contrib import admin 
from django.urls import path
from todolist.views import index, tasks_api

urlpatterns = [
    path('', index),
    path('api/tasks', tasks_api)
]