import codecs
codecs.register(XViewStateHandler())

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import base36_to_int
from django.template.loader import render_to_string
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib
