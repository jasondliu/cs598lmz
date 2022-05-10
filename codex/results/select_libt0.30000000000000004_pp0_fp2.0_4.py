import select
import sys
import time
import traceback
import types
import urllib
import urllib2
import urlparse

from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.core.handlers.wsgi import LimitedStream
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from django.utils.encoding import smart_str
from django.utils.functional import Promise
from django.utils.hashcompat import md5_constructor
from django.utils.http import urlquote
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt

from django_openid.models import UserOpenidAssociation
from django_openid.signals import openid_login_complete
from django_openid.store import DjangoOpenIDStore
from django_openid.util import
