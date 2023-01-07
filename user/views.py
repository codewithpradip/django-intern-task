from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Your Are login Successfully !!')
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect!!')

    form = UserLoginForm()
    return render(request, 'user/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You Are logout Successfully !!')
    return redirect("user_login")
