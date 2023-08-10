from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Profile, Post, LikePost, FollowersCount,Usermode
from itertools import chain
import random
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        phone=request.POST.get('phone')
        birthdate=request.POST.get('birthdate')
        city=request.POST.get('city')
        zipcode=request.POST.get('zipcode')
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                
                
                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, fullname=fullname,phone=phone,city=city,birthdate=birthdate,zipcode=zipcode)

                new_profile.save()
                
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
        
    

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def about(request):
    return HttpResponse('Hello There')

def faq(request):
    return HttpResponse('Hello There')

def search(request):
    return HttpResponse('Hello There')

def profile(request):
    return HttpResponse('Hello There')