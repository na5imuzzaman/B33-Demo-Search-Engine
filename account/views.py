from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from account.forms import UserRegistrationForm, LoginForm


def registration_view(request):

    """

    Handel registration machanism of new user.


    """


    if request.user.is_authenticated:
        return redirect('search')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
