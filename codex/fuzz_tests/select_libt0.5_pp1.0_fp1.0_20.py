import select
import socket
import sys
import threading
import time
import traceback

from django.conf import settings
from django.core import signals
from django.core.handlers.wsgi import WSGIHandler
from django.core.servers.basehttp import AdminMediaHandler, WSGIServerException, \
    WSGIRequestHandler, get_internal_wsgi_application
from django.core.servers.basehttp import DEFAULT_ERROR_CONTENT_TYPE, \
    DEFAULT_ERROR_CONTENT
from django.utils import autoreload
from django.utils.encoding import force_str

__all__ = ('WSGIServer', 'WSGIRequestHandler')

# Work around broken pipe errors once per handle_one_request()
# rather than on every request.
_brokenpipe_errors = 0

# Work around a Python 2.7.9 bug in http.server.BaseHTTPRequestHandler.
# See https://bugs.python.org/issue21724
_sendfile_version = getattr(sys, 'getwindowsversion', lambda: (0, 0
