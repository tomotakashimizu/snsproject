from django.urls import path
from .views import signupfunc, loginfunc

urlpatterns = [
    path('signup/', signupfunc),
    path('login/', loginfunc)
]
