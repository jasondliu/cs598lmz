import socket

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST

from django_openid_auth.models import UserOpenID
from django_openid_auth.views import make_consumer

from account.forms import AddEmailForm, ChangePasswordForm, ChangeTimezoneForm, \
    LoginForm, ResetPasswordForm, SetPasswordForm, SignupForm
from account.models import Account, EmailAddress, PasswordReset
from account.utils import default_redirect, get_form_data, perform_login, \
    send_email_confirmation
from account.views import _ajax_response
from pinax.apps.account.forms import ProfileForm
from pinax.apps.account.views import login as
