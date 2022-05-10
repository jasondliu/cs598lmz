import _struct
from ._struct import *
from warnings import warnpy3k


class StructError(TypeError):
    pass


def unpack(fmt, buffer):
    """Unpack from the buffer according to the format string fmt.

    Requires len(buffer) == calcsize(fmt).
    See help(struct) for more on format strings.
    """
    return _struct.unpack(fmt, buffer)


def calcsize(fmt):
    """Return size in bytes of the struct described by the format string fmt."""
    return _struct.calcsize(fmt)


def pack(fmt, *args):
    """Pack the values v1, v2, ... according to the format string fmt.
    See help(struct) for more on format strings.
    """
    return _struct.pack(fmt, *args)


def pack_into(fmt, buffer, offset, *args):
    """Pack the values v1, v2, ... according to the format string fmt.
    Writes the packed bytes into the writable buffer startint at offset.
   
