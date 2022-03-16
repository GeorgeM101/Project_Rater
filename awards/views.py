from django.shortcuts import render,redirect
from .models import Project,User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as signin


# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects':projects})

def register(request):
    if request.method=="POST":
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        e_username=User.objects.filter(username=username).count()
        email_exist=User.objects.filter(email=email).count()
        if e_username>0:
            messages.add_message(request, messages.ERROR, 'Username exist')
            return redirect(register)
        elif email_exist>0:
            messages.add_message(request, messages.ERROR, 'Email exist')
            return redirect(register)
        else:
            if password!=confirm_password:
                messages.add_message(request, messages.ERROR, 'Username exist')
                return redirect(register)
            else:
                user = User(username=username, email=email,phone_number=phone,password=make_password(password))
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Saved successfully!')
                return redirect(user_login)
    else:
        return render(request, "registration/register.html")

def user_login(request):
     if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email, password=password)
        if user is not None:
            signin(request,user )
            return redirect(index)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return redirect(user_login)
     else:
        return render(request, "registration/login.html")