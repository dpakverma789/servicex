from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signin(request):
    if request.method == 'POST' and request.POST:
        customer_contact = request.POST.get('contact')
        user_master_password = request.POST.get('password')
        if Customer.objects.filter(contact=customer_contact).count():
            users = authenticate(contact=customer_contact, password=user_master_password)
            if users is not None:
                login(request, users)
                return redirect('pass-manager-page')
            else:
                messages.error(request, 'Your Password is Incorrect!')
        else:
            messages.error(request, 'You are Not a User!')
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST' and request.POST:
        customer_first_name = request.POST.get('first_name').strip()
        customer_last_name = request.POST.get('last_name').strip()
        customer_address = request.POST.get('address').strip()
        customer_contact = request.POST.get('contact').strip()
        user_master_password = request.POST.get('password').strip()
        user_password_confirm = request.POST.get('password_confirm').strip()
        if user_master_password == user_password_confirm:
            if Customer.objects.filter(contact=customer_contact).count() == 0:
                users = Customer(firstname=customer_first_name, lastname=customer_last_name, address=customer_address)
                users.contact = customer_contact
                users.customer_id = str(customer_first_name)[:4]+str(customer_contact)[-4:]
                users.save()
                messages.success(request, 'Account successfully created!')
                return redirect('signin-page')
            else:
                messages.error(request, f'Account with \'{customer_contact}\' already exist')
        else:
            messages.warning(request, 'Confirm Password Didn\'t Matached')
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('signin-page')
