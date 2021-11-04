from .views import *
from django.urls import path


urlpatterns = [
    path('index/', index),
    path('home/', home),
    path('register/', register),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),
    path('login/', login),
    path('logout/', logout),
]