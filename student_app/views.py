from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .forms import RegistrationForm, ProfileUpdateForm
from .models import StudentProfile
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            password = form.cleaned_data.get('password')  
            user = User.objects.create_user(
                username=profile.roll_number,
                password=password
            )
            profile.user = user
            profile.save()
            
            send_mail(
                'Registration Successful',
                'You have been successfully registered! Please log in.',
                'rekhachowdary309@gmail.com',
                [profile.email],
                fail_silently=False,
            )

            messages.success(request, 'Registration successful! Check your email.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})


def display_data(request):
    session_id = request.session.get('session_id')  # Retrieve session_id safely
    data = StudentProfile.objects.all()
    return render(request, 'display_data.html', {'data': data, 'session_id': session_id})
def profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    session_id = request.session.get('session_id')
    roll_number = request.session.get('roll_number')

    print(f"Session ID: {session_id}, Roll Number: {roll_number}")  # Debugging log

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {
        'form': form, 
        'profile': profile, 
        'session_id': session_id, 
        'roll_number': roll_number
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not request.session.session_key:
                request.session.create()
            request.session['session_id'] = request.session.session_key  
            
            try:
                student = StudentProfile.objects.get(user=user)
                request.session['roll_number'] = student.roll_number
            except StudentProfile.DoesNotExist:
                messages.error(request, "User profile not found.")

            messages.success(request, f'Logged in successfully! Session ID: {request.session["session_id"]}')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'login.html')

def user_logout(request):
    request.session.pop('session_id', None)  # Safely remove session_id if it exists
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
