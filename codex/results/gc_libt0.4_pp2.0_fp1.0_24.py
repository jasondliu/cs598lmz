import gc, weakref

from . import _base
from . import _implementation
from . import _proxy

class _Proxy(object):
    """A weakrefable proxy for a C++ object.

    This is an implementation detail; do not use this class directly.

    """
    def __init__(self, ptr, factory):
        self._ptr = ptr
        self._factory = factory

    def __call__(self):
        """Return a strong reference to the proxied object.

        If the proxied object has been destroyed, this will return None.

        """
        return self._factory(self._ptr)

    def __eq__(self, other):
        return self._ptr == other._ptr

    def __hash__(self):
        return hash(self._ptr)

    def __repr__(self):
        return '<%s for %s>' % (self.__class__.__name__, self._ptr)


class _ProxyFactory(object):
    """A factory for weakrefable proxies to C++ objects.

    This is an implementation detail; do not use this class
