import weakref

from . import _ffi as ffi, _lib as lib


class _CDataMeta(type(ffi.CData)):
    """Metaclass for _CData."""

    def __new__(cls, name, bases, dct):
        # Add a classmethod to the class that returns the corresponding
        # C type object.
        if '_type_' in dct:
            dct['from_param'] = classmethod(lambda cls, x: cls._type_)
        return super().__new__(cls, name, bases, dct)


class _CData(_metaclass=_CDataMeta):
    """Base class for CData objects.

    This class is not meant to be instantiated directly.
    """

    def __init__(self, ptr=None, own=False):
        self._ptr = ptr
        self._own = own

    def __del__(self):
        if self._own:
            lib.free(self._ptr)

    def __repr__(self):
        return '<{}
