import socket
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegistrationForm
from .models import Post, User, Like, Follow
from .views.user_views import *
from .views.post_views import *
from .views.comment_views import *
from .views.like_views import *
from .views.follow_views import *

from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def fetch_login(request):
    return render(request, 'instagram_app/login.html')


def fetch_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Registration successfully!')

    #else:
    form = UserRegistrationForm()

    return render(request, 'instagram_app/registration.html', {'form': form})


def logout(request):
    auth.logout(request)
