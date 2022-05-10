import socket

try:
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib2 import HTTPError, URLError
    from urllib import urlencode
    from urllib2 import urlopen

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from pycas.backends import CASBackend
from pycas.decorators import require_login
from pycas.exceptions import CasTicketException
from pycas.models import Nonce
from pycas.views import login, logout


class PyCasTests(TestCase):

    def setUp(self):
        settings.LOGIN_URL = '/foo/'
        settings.CAS_SERVER_URL = 'http://example.com/cas'
        settings.CAS_EXTRA_LOGIN_PARAMS = []
        settings
