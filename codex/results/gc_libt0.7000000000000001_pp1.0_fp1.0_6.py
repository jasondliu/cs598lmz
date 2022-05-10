import gc, weakref
import threading

class WeakMethod(object):
    """
    A callable object that represents a weak reference to a function or method.
    """
    def __init__(self, method):
        self.method = self._get_method(method)

    def __call__(self, *args, **kwargs):
        if self.method is not None:
            return self.method(*args, **kwargs)

    def _get_method(self, method):
        try:
            return weakref.proxy(method)
        except TypeError:
            return None

    def __eq__(self, other):
        return self.method == self._get_method(other)

    def __ne__(self, other):
        return not self.__eq__(other)


class WeakMethodHandler(object):
    """
    A callable object that holds a weak reference to a function with a
    particular signature.  This is useful for using with callbacks, as it
    will automatically pass through any positional or keyword arguments
    that are provided.
    """
    def __init__
