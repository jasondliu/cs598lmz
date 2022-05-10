import weakref

from . import _util
from . import _wrap
from . import _core
from . import _types


class _Method(object):
    """
    A wrapper for a method of a PyObject.
    """

    def __init__(self, obj, method, flags):
        self._obj = obj
        self._method = method
        self._flags = flags

    def __call__(self, *args, **kwargs):
        return _core.py_call(self._obj, self._method, self._flags, args, kwargs)


class PyObject(object):
    """
    A wrapper for a PyObject.
    """

