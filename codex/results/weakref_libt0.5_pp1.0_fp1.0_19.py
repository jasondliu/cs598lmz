import weakref

from . import _utils
from . import _errors


class _WeakMethod(object):
    """
    A weak reference to a bound method.

    We need this because a normal weakref.ref() will not call
    the reference object's __del__ method when the object is garbage
    collected.
    """

    def __init__(self, fn):
        try:
            self.wr = weakref.ref(fn.__func__)
            self.obj = weakref.ref(fn.__self__)
        except AttributeError:
            self.wr = None
            self.obj = None

    def __call__(self):
        if self.wr is not None and self.obj is not None:
            obj = self.obj()
            if obj is not None:
                return types.MethodType(self.wr(), obj)


class _CallbackList(object):
    """
    A list of weak references to bound methods.
    """

    def __init__(self):
        self.callbacks = []

    def __iter__(self):
        return iter
