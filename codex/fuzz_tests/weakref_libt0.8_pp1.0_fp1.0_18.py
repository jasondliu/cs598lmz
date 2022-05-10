import weakref
import collections

_OLD_IS_WRAPPER = (2, 7) <= sys.version_info < (3, 2)


class WeakDescriptor(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return self.value(obj)


class WeakMethod:
    """A class for weak reference to unbound methods in Python"""
    def __new__(cls, obj, method):
        if obj is None:
            return None
        # If obj is not a class, a descriptor must already be stored in
        # method.__get__(obj, type(obj))
        assert inspect.ismethod(method), 'Need a method here'
        if inspect.isclass(obj):
            undefined = object()
            # Lookup in the class cache
            wr_method = cls._method_cache.get((id(type(obj)), method.__name__), undefined)
            if wr_method is undefined:
                # Cache
