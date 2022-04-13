from django.shortcuts import render

# Create your views here.


def signupfunc(request):
    return render(request, 'signup.html', {'some': 100})
