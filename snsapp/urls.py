from django.urls import path

from .views import (
    detailfunc,
    goodfunc,
    listfunc,
    loginfunc,
    logoutfunc,
    readfunc,
    signupfunc,
)

urlpatterns = [
    path("signup/", signupfunc, name="signup"),
    path("login/", loginfunc, name="login"),
    path("list/", listfunc, name="list"),
    path("detail/<int:pk>", detailfunc, name="detail"),
    path("logout/", logoutfunc, name="logout"),
    path("good/<int:pk>", goodfunc, name="good"),
    path("read/<int:pk>", readfunc, name="read"),
]
