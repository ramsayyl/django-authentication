from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

# Create your views here.
# View homepage by rendering out the home.html file which includes functionality
def home(request):
    return render(request, 'mysite/home.html')


def register(request):

    # When form is submitted with info
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        # Ensure each form field meets its requirements and create a new user with it
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']


            # If the user doesn't exist, create a user with the provided information then log them in
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)

                return HttpResponseRedirect('/')

            # Otherwise prompt the user that the name exists and allow them to enter info again
            else:
                # raise forms.ValidationError('Looks like a username with that email or password already exists')
                return HttpResponseRedirect('/')

    else:
        form = UserRegistrationForm()

    # Rerun the contents in register.html based on the logic in this method, and forms.py
    return render(request, 'mysite/register.html', {'form': form})
