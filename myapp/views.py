from django.shortcuts import render,redirect
from django.contrib import messages
from . form import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect,HttpRequest


# Sign-up function
def signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm= SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Registered Successfully')
                
        else:
            fm = SignUpForm()
        return render(request,'enroll/signup.html',{'form':fm})
    else:
        return redirect('/profile/')
# Login_view Function.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return redirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/login.html',{"form":fm})
    else:
        return redirect('/profile/')


# User Profile.
def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html', {'name':request.user.get_full_name})
    else:
        return redirect('/login/')

# Logout profile.
def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully Thanks for visiting our website.')
    return HttpResponseRedirect('/login/')
