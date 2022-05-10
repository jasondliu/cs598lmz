import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
import weakref
import operator

class Weak(object):
    """Keep a weak reference to an object.

    >>> o = object()
    >>> w = Weak(o)
    >>> o is w()
    True
    >>>
    >>> del o
    >>> w() is None
    True

    """

    def __init__(self, obj):
        self.weak = weakref.ref(obj)

    def __call__(self):
        return self.weak()

class _MFunc(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(args)

    def _getctypesargtypes(self, func=None, cfunctype=None):
        from .array_functions import ctypes_argtype
        if cfunctype is not None:
            return tuple(ctypes_argtype(at) for at in cfunctype.argtypes)
        if func is None:
            func = self.func
        if hasattr(func, '
