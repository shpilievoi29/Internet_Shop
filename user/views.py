from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from user.forms import UserRegistrationForm, UserLoginForm


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password1"),
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
            )
            redirect_url = reverse_lazy("login")
            return HttpResponseRedirect(redirect_url)
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "user/register.html", context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # user = authenticate(username=form.cleaned_data.get("username"),
            #                     password=form.cleaned_data.get("password"))
            # if user is None:
            login(request, form.user)
            redirect_url = reverse_lazy("product_list")
            return HttpResponseRedirect(redirect_url)
    else:
        form = UserLoginForm()
    return render(request, "user/login.html", {"form": form})


def user_logout(request):
    logout(request)
    logout_redirect = reverse_lazy(request, "/")

    return HttpResponseRedirect(request, logout_redirect)


def home(request):
    return render(request, "home.html")
