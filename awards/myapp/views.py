from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or Name)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usernam, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

@login_required
def index(request):
    return render('index.html')
