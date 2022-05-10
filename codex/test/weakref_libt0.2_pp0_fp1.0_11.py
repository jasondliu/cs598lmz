import weakref

from . import _base
from . import _compat
from . import _util

# pylint: disable=protected-access


class _WeakMethod(object):
    """
    A callable that proxies another callable, but weakly references it.

    This is useful for callbacks that are bound methods, so that the object
    doesn't have to be kept alive just to call the method later.

    This class is not thread-safe.
    """
    def __init__(self, callback):
        self._callback_ref = weakref.ref(callback.__self__)
        self._callback_func = callback.__func__

    def __call__(self, *args, **kwargs):
        callback = self._callback_ref()
        if callback is not None:
            return self._callback_func(callback, *args, **kwargs)


class _Event(object):
    """
    A single event.

    This class is not thread-safe.
    """
    def __init__(self):
        self._listeners = []

