import codecs
codecs.register_error("strict", codecs.ignore_errors)

from .settings import MEDIA_ROOT, MEDIA_URL
from .settings import STATIC_ROOT, STATIC_URL
from .settings import STATICFILES_FINDERS, TEMPLATE_LOADERS
from .settings import TEMPLATE_DIRS, MIDDLEWARE_CLASSES
from .settings import ROOT_URLCONF, APPEND_SLASH
from .settings import CACHE_BACKEND, CACHE_MIDDLEWARE_KEY_PREFIX


from django.utils.importlib import import_module
from django.utils.log import getLogger


def get_cache():
    """
    Returns the cache used by Django. This can be used by standalone
    Django applications. If no cache is configured, this returns a dummy
    cache that doesn't do anything.
    """
    if CACHE_BACKEND is None:
        from django.core.cache import get_cache as gc
        cache = gc('dummy://')
        cache.add = lambda x, y:
