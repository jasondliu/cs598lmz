import weakref

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet
from django.utils.importlib import import_module


class Cached(object):
    """A descriptor that caches the result of the first call to the wrapped
    function. If the function is called with arguments, it is assumed that
    the cached value is no longer valid.
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if not hasattr(instance, '_cache'):
            instance._cache = {}

        if self.func not in instance._cache:
            instance._cache[self.func] = self.func(instance)

        return instance._cache[self.func]

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Cached
