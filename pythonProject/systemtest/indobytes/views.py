from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.


def home(request):
    employee = Indobyte_employees.objects.all()
    details = {'emp_data': employee}
    return render(request, 'home.html', details)


def userregistration(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            image = request.POST.get('image')
            gender = request.POST.get('gender')
            Education = request.POST.get('Education')
            favorite_hobbies = request.POST.get('favorite_hobbies')

            if password == confirmpassword:
                user = User.objects.create_user(username=name, email=email, password=password)
                UserDetails.objects.create(mobile=mobile, address=address, user=user)
                send_mail('Thank you ' + name + ' for registration',
                          'Here is your login Below \nhttp://127.0.0.1:9000/indobytes/login/',
                          settings.EMAIL_HOST_USER,
                          [email]
                          )
                return redirect('/login/')
    form = UserDetailsForm()
    return render(request, 'userregistration.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'userlogin.html', {'comment': 'Enter Valid details'})
    return render(request, 'userlogin.html')


def userlogout(request):
    logout(request)
    return redirect('/login/')
