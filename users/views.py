from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import requests

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance = request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your profile has been updated')
      return redirect('portfolio')
  else:
    u_form = UserUpdateForm(instance = request.user)
    p_form = ProfileUpdateForm(instance = request.user.profile)

  context = {
    'u_form' :  u_form,
    'p_form' :  p_form,
  }

  return render(request, 'registration/profile.html', context)


def createdashboard(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4b4857337408a4e1fe365b3bfdc7374d'
  city = 'Guwahati'
  city_weather  = requests.get(url.format(city)).json()

  weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

  context = {'weather' : weather}

  return render(request, 'dashboard.html', context) #returns the index.html template
