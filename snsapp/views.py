from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def signupfunc(request):
    object = User.objects.get(username='tomo')
    print(object.email)
    if request.method == "POST":
        print('this is post method')
    else:
        print('this is not post method')
    return render(request, 'signup.html', {'some': 100})
