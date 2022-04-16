from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def signupfunc(request):
    print(request.POST)
    return render(request, 'signup.html', {'some': 100})
