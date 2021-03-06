from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def root(request):
    return render(request, 'index.html')

def process_registration(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password=request.POST['password']
        pw_hash=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        request.session['email']=request.POST['email']
    return redirect('/dashboard')

def process_login(request):
    user=User.objects.filter(email=request.POST['email'])
    if user:
        context={
            'email':User.objects.get(email=request.POST['email']).email
        }
        request.session['email']=context['email']
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid']=logged_user.id
            return redirect('/dashboard')
    errors={}
    errors['password']="Email and/or password did not match our records"
    for key, value in errors.items():
        messages.error(request, value)
    return redirect('/')