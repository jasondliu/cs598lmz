import gc, weakref
from _weakref import ref as _ref

from itertools import chain

try:
    from _weakref import proxy as _proxy
except ImportError:
    class _proxy(object):
        __slots__ = ("_obj", "_callback")
        def __new__(cls, ob, callback=None):
            self = object.__new__(cls)
            self._obj = ob
            self._callback = callback
            return self
        def __call__(self):
            return self._obj
        def __hash__(self):
            return hash(self._obj)
        def __setattr__(self, attr, value):
            if attr == "_obj" or not hasattr(self._obj, attr):
                raise AttributeError("%r object has no attribute %s" % (type(self).__name__, attr))
            setattr(self._obj, attr, value)
        def __delattr__(self, attr):
            if attr == "_obj" or not hasattr(self._obj, attr):
               
