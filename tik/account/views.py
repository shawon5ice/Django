from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
  if request=='POST':
    first_name = request.POST['f_name']
    last_name = request.POST['l_name']
    username = request.POST['u_name']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    email = request.POST['email']

    if pass1==pass2:
      if User.objects.filter(username=username).exists():
        print('user name taken')
      elif User.objects.filter(email=email).exists():
        print('email already used')
      else:
        user = User(first_name=first_name,last_name=last_name,username=username,email=email,password=pass1)
        user.save()
        print('user created')
    else:
      print('password not matched')
    return redirect('/')
  else:
    return render(request,'register.html')