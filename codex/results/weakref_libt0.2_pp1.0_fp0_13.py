import weakref

from . import _core
from . import _util
from . import _wrap
from . import _wrap_util

#------------------------------------------------------------------------------
# Python object wrapper.

class PythonObjectWrapper(object):
    """
    Wraps a Python object.
    """

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name == '_obj':
            self.__dict__[name] = value
        else:
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        delattr(self._obj, name)

    def __call__(self, *args, **kwargs):
        return self._obj(*args, **kwargs)

    def __repr__(self):
        return repr(self._obj)

    def __str__(self):
        return str(self._obj)

    def __hash__(self):

