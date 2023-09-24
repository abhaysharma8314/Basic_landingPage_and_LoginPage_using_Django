from django.contrib import admin
from django.urls import path,include
from new import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services')
]

