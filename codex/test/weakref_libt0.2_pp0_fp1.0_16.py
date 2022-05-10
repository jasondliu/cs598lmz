import weakref

from . import _base
from . import _compat
from . import _util
from . import _types


class _Type(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


class _TypeInfo(object):
    def __init__(self, name, type, *args, **kwargs):
        self.name = name
        self.type = type
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


