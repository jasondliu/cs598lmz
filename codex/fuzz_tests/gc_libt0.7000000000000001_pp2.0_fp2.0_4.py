import gc, weakref
import sys
import threading
import time
import traceback

from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.core.signals import request_finished
from django.dispatch import dispatcher
from django.utils.cache import patch_vary_headers
from django.utils.importlib import import_module
from django.utils import translation

# Configure logging for the first time
import logging
logger = logging.getLogger('django.request')

__all__ = ('BaseHandler', 'WSGIHandler')

class BaseHandler(object):
    """
    A base class to handler requests.

    Subclasses must implement the __call__ method, which takes an HttpRequest
    and returns an HttpResponse.
    """

    initLock = threading.Lock()
    request_class = HttpRequest # The request class to use.
