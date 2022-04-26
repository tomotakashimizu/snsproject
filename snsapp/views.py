from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from .models import SnsModel

# Create your views here.


def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return render(request, "signup.html", {"some": 100})
        except IntegrityError:
            return render(request, "signup.html", {"error": "このユーザーはすでに登録されています。"})
    return render(request, "signup.html", {"some": 100})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html", {})
    return render(request, "login.html", {})


# ログイン状態判定し画面遷移
@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, "list.html", {"object_list": object_list})


def logoutfunc(request):
    logout(request)
    return redirect("login")


def detailfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    return render(request, "detail.html", {"object": object})
