import _struct

from . import _error
from ._common import _decode_utf8, _encode_utf8, _str_to_bytes, _warn_bytes_env


class Struct(_struct.Struct):
    """Wrapper class for _struct.Struct to extend the format string
    with support for native 'l' and 'L' types on 32-bits systems.
    """

    def __init__(self, fmt):
        _struct.Struct.__init__(self, fmt.replace('l', 'i').replace('L', 'I'))


def unpack_from(fmt, buffer, offset=0):
    """Read from buffer starting at offset according to the format string
    fmt and return a tuple of values.
    """
    s = Struct(fmt)
    size = s.size
    return s.unpack_from(buffer, offset)


def pack_into(fmt, buffer, offset, *args):
    """Write values into buffer starting at offset according to the format
    string fmt.
    """
    s = Struct(fmt)
    size = s
