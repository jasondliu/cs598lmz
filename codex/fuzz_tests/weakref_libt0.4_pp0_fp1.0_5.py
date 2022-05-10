import weakref
import logging
from . import _utils
from . import _constants
from . import _errors
from . import _wrapper
from . import _objects
from . import _enums

__all__ = ["Base", "BaseWrapper", "BaseObject", "BaseObjectWrapper", "BaseObjectRef", "BaseObjectRefWrapper"]

class Base(object):
    """
    Base class for all objects.
    """
    def __init__(self, *args, **kwargs):
        self._log = logging.getLogger("enigma2.Base")
        self._log.debug("__init__()")
        self._args = args
        self._kwargs = kwargs

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self.__dict__)

    def __str__(self):
        return self.__repr__()

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
