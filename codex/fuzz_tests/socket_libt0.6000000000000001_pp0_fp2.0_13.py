import socket, threading, time
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.template import loader
from django.http import StreamingHttpResponse
from .models import *
from .forms import *
from .utils import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_
