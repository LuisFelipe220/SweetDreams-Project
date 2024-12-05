"""
URL configuration for SweetDreams project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sleep_helper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('activities/', views.activities, name='activities'),
    path('feedback/', views.feedback, name='feedback'),
    path('meditation/', views.meditation, name='meditation'),
    path('physicalActivity/', views.physicalActivity, name='physicalActivity'),
    path('relaxButton/', views.relaxButton, name='relaxButton'),
    path('meditationEasy/', views.meditationEasy, name='meditationEasy'),
    path('meditationIntermediate/', views.meditationIntermediate, name='meditationIntermediate'),
    path('meditationAdvanced/', views.meditationAdvanced, name='meditationAdvanced'),
    path('pilatesActivity/', views.pilatesActivity, name='pilatesActivity'),
    path('yogaActivity/', views.yogaActivity, name='yogaActivity'),
    path('breathingTechniquesActivity/', views.breathingTechniquesActivity, name='breathingTechniquesActivity'),
    path('soundOfRain/', views.soundOfRain, name='soundOfRain'),
    path('staticNoise/', views.staticNoise, name='staticNoise'),
    path('waterfallSound/', views.waterfallSound, name='waterfallSound'),
]

