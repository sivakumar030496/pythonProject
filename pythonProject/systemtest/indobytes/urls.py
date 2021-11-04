from django.urls import path
from .views import *

urlpatterns = [

    path("home/", home),
    path('register/', userregistration),
    path('login/', userlogin),
    path('logout/', userlogout),
]
