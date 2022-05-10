import weakref

from . import _base


class _WeakMethod(object):
    """
    A weak reference to a bound method, working around the lifetime
    problem of bound methods.

    When a bound method goes out of scope, the object it is bound to is
    kept alive. This creates a reference cycle that cannot be broken by
    the garbage collector.

    This class solves the problem by storing a weak reference to the
    object as well as the function and the instance the method is bound
    to.
    """
    def __init__(self, func, obj):
        self.func = func
        self.obj = weakref.ref(obj)

    def __call__(self):
        obj = self.obj()
        if obj is not None:
            return self.func.__get__(obj, obj.__class__)


class _WeakMethodDict(_base.WeakMethodDict):
    """
    A dict that stores weak references to the methods as values.
    """
    def __init__(self):
        self._dict = weakref.WeakValueDictionary()

    def __
