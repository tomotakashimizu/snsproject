from django.urls import path

from .views import PostCreate, detailfunc, goodfunc, listfunc, loginfunc, logoutfunc, readfunc, signupfunc

urlpatterns = [
    path("signup/", signupfunc, name="signup"),
    path("login/", loginfunc, name="login"),
    path("list/", listfunc, name="list"),
    path("detail/<int:pk>", detailfunc, name="detail"),
    path("create/", PostCreate.as_view(), name="create"),
    path("logout/", logoutfunc, name="logout"),
    path("good/<int:pk>", goodfunc, name="good"),
    path("read/<int:pk>", readfunc, name="read"),
]
