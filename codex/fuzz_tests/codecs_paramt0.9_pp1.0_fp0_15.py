import codecs
codecs.register_error("ignore", codecs.replace_errors)
import inspect

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext
from django.urls import reverse
from django.db.models import Q
from django.conf import settings

from django.utils.timezone import now

from appconf.manager import SettingManager
from utilities.mail import send_mail
from utilities.json import json_response, json_error

from .forms import MessageForm


def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if settings.DEBUG:
                print('Captcha Valid:',request.recaptcha_is_valid)
            else:
                if not request.recaptcha_is_valid:
                    return HttpResponseRedirect(reverse("index") + "?captcha_error=1")
            body = settings.EMAIL_CONTACT_B
