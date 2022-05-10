import types
types.FunctionType = types.BuiltinFunctionType = lambda x: True

from django.apps import apps

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, MiddlewareNotUsed
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule
from django.utils import six

from django.core.urlresolvers import get_resolver, RegexURLPattern, RegexURLResolver
from django.core.urlresolvers import get_script_prefix, get_urlconf, set_script_prefix
from django.core.urlresolvers import clear_url_caches, resolve, reverse, NoReverseMatch

from django.utils.encoding import force_text
from django.utils.functional import lazy, memoize
