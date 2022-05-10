import weakref

from . import (
    _util,
    _constants,
    _errors,
)

class _Base(_util.Base):
    """
    Base class for all objects in the library.
    """
    def __init__(self, handle, core_object):
        if not isinstance(handle, int):
            raise TypeError("Expected handle to be an int, got %s" % type(handle))
        if not isinstance(core_object, bool):
            raise TypeError("Expected core_object to be a bool, got %s" % type(core_object))
        self._handle = handle
        self._core_object = core_object

    def __eq__(self, other):
        if not isinstance(other, _Base):
            return False
        return self._handle == other._handle

    def __ne__(self, other):
        if not isinstance(other, _Base):
            return True
        return self._handle != other._handle

    def __hash__(self):
        return hash(self._handle)

    @property

