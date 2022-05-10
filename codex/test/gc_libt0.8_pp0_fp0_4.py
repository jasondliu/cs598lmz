import gc, weakref, sys

_UNSET = object()

class _BuiltinMethod(object):
    def __init__(self, name):
        self.__name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        try:
            return getattr(obj._obj, self.__name)
        except AttributeError:
            raise NotImplementedError

