import weakref
import re
import logging

from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.test import TestCase
from django.utils.importlib import import_module
from django.test.client import Client, RequestFactory
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from .models import (Access, AccessToken, AuthorizationCode, Client,
                     get_application_model, get_access_token_model,
                     RefreshToken, get_refresh_token_model, Grant,
                     get_grant_model)
from .settings import oauth2_settings
from .views import ProtectedResourceView
from .backends import OAuth2Backend


Application = get_application_model()
Grant = get_grant_model()
AccessToken = get_access_token_model()
RefreshToken = get_refresh_token_model()


