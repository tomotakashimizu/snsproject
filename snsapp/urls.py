from django.urls import path

from .views import detailfunc, listfunc, loginfunc, logoutfunc, signupfunc

urlpatterns = [
    path("signup/", signupfunc, name="signup"),
    path("login/", loginfunc, name="login"),
    path("list/", listfunc, name="list"),
    path("logout/", logoutfunc, name="logout"),
    path("detail/<int:pk>", detailfunc, name="detail"),
]
