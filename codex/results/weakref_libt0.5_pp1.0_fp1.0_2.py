import weakref

from . import _ffi
from . import _lib
from . import _util

from . import _cffi_base_backend
from . import _cffi_opcode
from . import _cffi_utils


class _CData(object):
    __slots__ = ['_cffi_ref', '_cffi_keep']
    _cffi_ref = None
    _cffi_keep = None

    def __init__(self, ptr):
        self._cffi_ref = ptr

    def __del__(self):
        if self._cffi_ref:
            _lib.Py_DecRef(self._cffi_ref)
            self._cffi_ref = None

    def __repr__(self):
        return '<CData %s owning %s>' % (self.__class__.__name__,
                                         self._cffi_ref)

    def __str__(self):
        return repr(self)

    def __nonzero__(self):
        return bool
