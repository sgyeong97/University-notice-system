from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, ProfileForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/notice')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def profile(request, pk):
    instance = get_object_or_404(User, id=pk)
    form = ProfileForm(request.POST or None, instance=instance.profile)
    if form.is_valid():
        form.save()
        return redirect('/notice')
    return render(request, 'accounts/profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/notice')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
