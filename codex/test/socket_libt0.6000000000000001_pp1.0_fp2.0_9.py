import socket
import urllib
import urllib2
import urlparse

try:
    import json
except ImportError:
    import simplejson as json

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.utils.encoding import smart_str
from django.utils.http import urlquote
from django.utils.translation import ugettext as _

from social_auth.backends import BaseOAuth, OAuthBackend, USERNAME
from social_auth.exceptions import AuthCanceled, AuthUnknownError, AuthMissingParameter
from social_auth.utils import setting, log, dsa_urlopen


# facebook configuration
FACEBOOK_SERVER = 'graph.facebook.com'
FACEBOOK_AUTHORIZATION_URL = 'https://%s/oauth/authorize' % FACEBOOK_SERVER
