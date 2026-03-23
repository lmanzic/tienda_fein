from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('catalog')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenid@ {user.first_name or user.username}!')
            return redirect(request.GET.get('next', 'catalog'))
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, '¡Hasta pronto!')
    return redirect('catalog')
