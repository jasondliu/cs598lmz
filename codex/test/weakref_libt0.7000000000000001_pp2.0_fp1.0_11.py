import weakref
from contextlib import contextmanager
from collections import OrderedDict
from functools import wraps
from six.moves import _thread

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
from django.utils.translation import get_language
from django.utils.translation.trans_real import parse_accept_lang_header

from . import middleware, translation


class LocaleURLMiddleware(middleware.LocaleURLMiddleware):
    """
    The middleware class. Adds support for translating URLs.
    """

    def __init__(self, get_response=None):
        self.url_name_prefixes = getattr(settings, 'LOCALEURL_USE_ACCEPT_LANGUAGE', False)
