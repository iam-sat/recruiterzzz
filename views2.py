from django.shortcuts import redirect, render
from django.contrib.auth import auth

def login(request):

    if request.method=='POST':
        email1=request.POST('email')
        password1=request.POST('password')
        x=auth.authenticate(email=email1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('index')
    else:   
        return render(request,'login.html')