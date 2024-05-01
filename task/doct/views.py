import email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import SignRegistrationForm
from .models import Sign


def home(request):
    if request.user.is_anonymous:
       return redirect("login/")
    return render(request, 'home.html')

def sign(request):
    if request.method == 'POST':
        form = SignRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other page after successful form submission
            return redirect('home')
    else:
        form = SignRegistrationForm()
    return render(request, 'doctor.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Sign

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve the user from the sign model using the provided username
        try:
            user = Sign.objects.get(username=username)
        except Sign.DoesNotExist:
            user = None

        if user is not None:
            # If the provided password matches the password stored in the sign model
            if user.password == password:
                # Redirect the user to the home page
                return redirect('home')  # Replace 'home' with the name of your home page URL pattern
            else:
                # If the passwords don't match, display an error message
                error_message = "Invalid password. Please try again."
        else:
            # If the username doesn't exist in the sign model, display an error message
            error_message = "Invalid username. Please try again."

        return render(request, 'login.html', {'error_message': error_message})

    # If the request method is GET, render the login page
    return render(request, 'login.html')





"""
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        sign = authenticate(request, username=username, password=password)
        if sign is not None:
           
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page with error message
    return render(request, 'login.html')  # Render login page for GET requests
"""






