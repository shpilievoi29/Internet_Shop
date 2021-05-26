from django.urls import path

from user.views import user_register, user_login, home

urlpatterns = [
    path("registration/", user_register, name="registration"),
    path("login/", user_login, name="login"),
    path("", home, name="home"),
]