from django.shortcuts import render, redirect
from django.contrib.auth.models import UserManager
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, HttpResponse
from new.models import Contact
from datetime import datetime
from django.contrib import messages

# password for test user is Harry$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

# Create your views here.
def about(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'about.html')
    #return HttpResponse("this is the about page")
def services(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'services.html')
    #return HttpResponse("this is the services page")
def contact(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    elif request.method =='POST':
        email = request.POST.get('email')
        suggestion = request.POST.get('suggestion')
        contact = Contact(email=email, suggestion=suggestion, date= datetime.today())
        contact.save()
        messages.success(request, "The message has been sent!")
    return render(request,'contact.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/login")


    
    #return HttpResponse("this is the contact page")