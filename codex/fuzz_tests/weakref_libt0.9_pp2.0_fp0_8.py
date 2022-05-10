import weakref
import threading

from django.conf import settings

from ratelimit.registry import Registry
from ratelimit.backends import cache_key, ALL
from ratelimit.backends.base import NotRatelimited
from ratelimit.decorators import ratelimit as _ratelimit

from .models import Entry, BlacklistedDomain


registry = Registry()


def ratelimit(key):
    """Wraps :func:`ratelimit.decorators.ratelimit` to use settings from the
    database.

    """
    settings, ratelimit_key = registry.get_ratelimit_settings(key)
    blacklist_enabled = (
        not settings.get('blacklist_enabled') or not
        BlacklistedDomain.objects.filter(domain=ratelimit_key).exists())
    if not blacklist_enabled:
        return NotRatelimited
    else:
        return _ratelimit(
            settings['hits'], settings['minutes'], settings['group'],
            settings['fail_silently'], key=ratelimit_key,
            ip=ratelimit_key.endswith
