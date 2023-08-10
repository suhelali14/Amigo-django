from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('faq', views.faq,name='faq'),
    path('search', views.search,name='search'),
    path('profile', views.profile,name='profile'),
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),

]