
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signup(request):
    if request.method=='POST': 
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        x=User.objects.create_user(name=name, email=email, password=password)
        x.save()
        print('User Created')
        return redirect('login.html')
    else:
        return render(request, signup.html)