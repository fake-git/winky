from django.shortcuts import render, redirect, reverse
from app.forms import LoginForm, RegisterForm
from app.models import User
from django.contrib import messages
from .utils import *
from django.db.models import Q


def register(request):
    print('asdsadasddasdadasd33333')

    if request.method == 'POST':
        print('7777777777777777777777777777777')

        form = RegisterForm(request.POST)
        if form.is_valid():

            if User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.warning(request, f"{form.cleaned_data['email']} is already in exists")
                return redirect(reverse('register'))

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       email=email,
                                       password=generateHash(password))
            if user:
                messages.success(request, 'Signup successful')
                return redirect(reverse('login_user'))
            else:
                messages.error(request, "Error in register function")
    else:
        form = RegisterForm()

    return render(request, 'Register.html', {'form': form})


#
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('asdsadasddasdadasd')
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed_pass = generateHash(password)

            if User.objects.get(Q(email=email), Q(password=hashed_pass)):  # we need to handle the exception
                user = User.objects.get(email=email)

                #if hashed_pass == user.get_pass():
                #login(request, user)
                messages.success(request, 'You are logged in')
                return redirect(reverse('products')) ## change that
            else:
                messages.error(request, 'Bad authentication')
                return redirect(reverse('login_user'))
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})

