import _struct

from . import util
from . import _util
from . import _ffi
from . import _lib


class _SodiumError(Exception):
    pass


class _SodiumLibraryError(_SodiumError):
    pass


class _SodiumMemoryError(_SodiumError):
    pass


class _Memoryview(memoryview):
    def __new__(cls, value, *args, **kwargs):
        if isinstance(value, _ffi.CData):
            value = _ffi.buffer(value)
        return memoryview.__new__(cls, value, *args, **kwargs)

    def __delitem__(self, key):
        raise NotImplementedError(
            "Memoryviews backed by cdata objects may not be modified"
        )

    def __setitem__(self, key, value):
        raise NotImplementedError(
            "Memoryviews backed by cdata objects may not be modified"
        )


def _check(return_code):
    if return_code != 0:
        raise _SodiumLibraryError
