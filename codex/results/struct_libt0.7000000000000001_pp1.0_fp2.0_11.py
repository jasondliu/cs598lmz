import _struct
from _struct import pack, unpack
from _struct import Struct
from _struct import calcsize

from _codecs import ascii_decode, ascii_encode, ascii_errors


def pack_into(fmt, buffer, offset, *args):
    """Pack the values v1, v2, ... according to the format string fmt.
    Write the packed bytes into the writable buffer starting at position
    offset.  Return the number of bytes written (which is the length of the
    packed bytes).
    """
    size = calcsize(fmt)
    buffer[offset:offset+size] = pack(fmt, *args)
    return size


def unpack_from(fmt, buffer, offset=0):
    """Unpack from the buffer starting at position offset according to the
    format string fmt.  Requires that the buffer length be at least offset +
    the size of the unpacked result.  Returns a tuple of the unpacked values.
    """
    size = calcsize(fmt)
    return unpack(fmt, buffer[
