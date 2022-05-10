import weakref

from zope import interface

from .. import interfaces
from ..util import get_property_cache, set_property_cache
from ..util import get_property_value, set_property_value

from . import _util as util


class Field(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.deferred = kwargs.get("deferred", False)
        self.default = kwargs.get("default", None)
        self._interface = kwargs.get("interface", None)
        self._may_read = kwargs.get("may_read", False)

    def __get__(self, obj, klass):
        if obj is None:
            return self
        return get_property_cache(obj, self.name, self.default)

    def __set__(self, obj, value):
        set_property_cache(obj, self.name, value)
