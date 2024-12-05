from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Email ou senha inválidos.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required()
def activities(request):
    return render(request, 'activities.html')

@login_required()
def feedback(request):
    return render(request, 'feedback.html')

@login_required()
def meditation(request):
    return render(request, 'meditation.html')

@login_required()
def physicalActivity(request):
    return render(request, 'physicalActivity.html')

@login_required()
def relaxButton(request):
    return render(request, 'relaxButton.html')

@login_required()
def meditationEasy(request):
    return render(request, 'meditationEasy.html')

@login_required()
def meditationIntermediate(request):
    return render(request, 'meditationIntermediate.html')

@login_required()
def meditationAdvanced(request):
    return render(request, 'meditationAdvanced.html')

@login_required()
def pilatesActivity(request):
    return render(request, 'pilatesActivity.html')

@login_required()
def yogaActivity(request):
    return render(request, 'yogaActivity.html')

@login_required()
def breathingTechniquesActivity(request):
    return render(request, 'breathingTechniquesActivity.html')

@login_required()
def soundOfRain(request):
    return render(request, 'soundOfRain.html')

@login_required()
def staticNoise(request):
    return render(request, 'staticNoise.html')

@login_required()
def waterfallSound(request):
    return render(request, 'waterfallSound.html')