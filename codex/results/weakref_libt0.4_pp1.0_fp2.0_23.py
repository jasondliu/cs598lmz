import weakref

from . import _core
from . import _util
from . import _ffi as _cffi

from . import _vendor
from . import _vendor.six as _six

from . import _vendor.numpy as _numpy

from . import _vendor.dataclasses as _dataclasses

from . import _vendor.typing as _typing


class _Base(object):
    """
    Base class for all objects in the API.
    """
    __slots__ = ()


class _CDataWrapper(_Base):
    """
    Base class for all objects wrapping a C data pointer.
    """
    __slots__ = ("_cdata",)

    def __init__(self, cdata):
        self._cdata = cdata

    def __del__(self):
        # The CFFI wrapper doesn't call __del__ when the object is garbage
        # collected, so we have to do it ourselves.
        self._free()

    def _free(self):
        """
        Free the C data pointer.
