from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        registration_form = CustomRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, ('User Account has been created!'))
            return redirect('user:register')
    else:
        registration_form = CustomRegisterForm()
    return render(request, 'register.html', {'registration_form': registration_form})
