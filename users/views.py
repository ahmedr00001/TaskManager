from django.shortcuts import render, redirect
from django.contrib import messages  # For system messages
from .models import User
from django.contrib.auth.hashers import check_password, make_password  # For password hashing
import time 
from .tasks import sent_emails


def login(request):

    # sent_emails.delay()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            # Use Django's check_password for secure password checking
            if check_password(password, user.password):  
                request.session['user_id'] = user.id  
                request.session['user_role'] = user.role  
                request.session['user_name'] = f"{user.first_name} {user.last_name}"  # Store full name in session

                messages.success(request, "Login successful!")  # Success message

                if user.role == 'manager':
                    return redirect('tasks:manager_tasks')
                elif user.role == 'employee':
                    return redirect('tasks:employee_tasks')
            else:
                messages.error(request, 'Invalid password')  
        except User.DoesNotExist:
            messages.error(request, 'User not found')  

        return render(request, 'users/login.html')  # Reload the login page with error messages
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        category = request.POST.get('category')
        phone_number = request.POST.get('phone_number')
        birthday = request.POST.get('birthday')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'users/register.html')  # Reload the register page with error message

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'users/register.html')  # Reload the register page with error message

        # Hash the password before saving
        hashed_password = make_password(password)

        user = User(
            first_name=first_name,
            last_name=last_name,
            category = category,
            email=email,
            phone_number=phone_number,
            birthday=birthday,
            role=role,
            password=hashed_password  # Store hashed password
        )
        user.save()

        messages.success(request, 'Registration successful! You can now login.')
        return redirect('users:login')  # Redirect to login page after successful registration

    return render(request, 'users/register.html')


def change_password(request):
    if request.method == "POST":
        user_id = request.session.get('user_id')  
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(id=user_id)

        if not check_password(old_password, user.password):
            messages.error(request, "Old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
        else:
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password updated successfully!")
            return redirect('users:login')  # or any page you want

    return render(request, 'users/change_password.html')


