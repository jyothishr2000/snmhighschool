from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import student

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def log(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pas']
        user=auth.authenticate(username=uname,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        msg="Invalid Username or Password"
        return render(request,'login.html',{'msg': msg})
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        ename=request.POST['ename']
        password=request.POST['pas']
        repassword=request.POST['repas']
        if password==repassword:
            if User.objects.filter(username=uname):
                msg='Username already exists'
                return render(request,'register.html',{'msg': msg})
            elif User.objects.filter(email=ename):
                msg='E-mail address already exists'
                return render(request,'register.html',{'msg': msg})
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=password)
                user.save();
                auth.login(request,user)
                return redirect ('/')
        else:
            msg='Invalid password'
            return render(request,'register.html',{'msg': msg})
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def admission(request):
    ad_no=request.POST['ad_no']
    name=request.POST['']
    age=request.POST['']
    place=request.POST['']
    subject=request.POST['']
    gname=request.POST['']
    dob=request.POST['']
    contact=request.POST['']
    email=request.POST['']
    return render(request,'admission.html')

def list(request):
    obj=student.objects.all()
    return render(request,'list.html',{'data':obj})

