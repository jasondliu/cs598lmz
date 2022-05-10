import weakref

from . import _lib
from . import _ffi
from . import _util
from . import _errors
from . import _types
from . import _compat


class _Base(object):
    """
    Base class for all libgit2 objects.
    """

    def __init__(self, ptr, owned=True):
        """
        Initialize a new object.

        :param ptr: A pointer to the underlying C structure
        :param owned: Whether the pointer is owned by this object
        """
        self._ptr = ptr
        self._owned = owned
        self._weakref = None

    def __del__(self):
        if self._owned and self._ptr:
            self._free(self._ptr)

    def __eq__(self, other):
        if not isinstance(other, _Base):
            return NotImplemented
        return self._ptr == other._ptr

    def __ne__(self, other):
        if not isinstance(other, _Base):
            return NotImplemented
        return self._ptr != other._ptr

