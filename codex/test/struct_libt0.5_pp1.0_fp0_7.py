import _struct
from . import _common
from . import _io

from . import _io


__all__ = [
    "error",
    "unpack",
    "unpack_from",
    "pack",
    "pack_into",
    "iter_unpack",
    "calcsize",
    "Struct",
]

_clearcache = _struct.__clearcache
_clearcache()

error = _struct.error


def _compile(fmt):
    code = _struct.calcsize(fmt)
    if code > 0:
        return _struct.compile(fmt)
    else:
        raise error("bad char in struct format")


def pack(fmt, *args):
    """
    Return a bytes object containing the values v1, v2, ... packed according
    to the format string fmt.  The arguments must match the values required by
    the format exactly.
    """
    return _struct.pack(_compile(fmt), *args)

