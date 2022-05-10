import weakref

from . import _core
from . import _util
from . import _enums

class _Object(object):
    """
    Base class for all objects.
    """
    __slots__ = ('_handle', '_weakref_cb')

    def __init__(self, handle):
        self._handle = handle
        self._weakref_cb = None

    def __del__(self):
        if self._handle is not None:
            _core.delete(self._handle)

    def __repr__(self):
        return '<{0} object at 0x{1:x}>'.format(
            self.__class__.__name__, id(self))

    def __str__(self):
        return repr(self)

    def __hash__(self):
        return hash(self._handle)

    def __eq__(self, other):
        if not isinstance(other, _Object):
            return NotImplemented
        return self._handle == other._handle

    def __ne__(self, other):
        if not is
