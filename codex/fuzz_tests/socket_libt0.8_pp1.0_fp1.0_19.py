import socket
import sys
from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import (clear_url_caches, get_callable,
                                      get_resolver, get_script_prefix)
from django.core.urlresolvers import Resolver404, resolve, resolve_url
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils.encoding import iri_to_uri
from django.utils.functional import lazy
from django.utils.http import urlencode, urlquote
from django.utils.six.moves.urllib.parse import parse_qs

from staticfiles.utils import check_settings

# Identifies Django's default request object
_thread_locals = threading.local()


def get_current_request():
    """
    Returns the current request object, if any.
    """
    return getattr(_thread_locals, "request", None)


