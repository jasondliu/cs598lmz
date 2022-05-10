import _struct as struct
from _struct import unpack, pack

def _is_little_endian():
    return sys.byteorder == 'little'

def _check_bytes(n):
    """
    Check that the argument is a bytes object with length 1, 2, 4, or 8.

    Raise a TypeError if it is not, or if it is a bytes object but has the
    wrong length.

    No return value.
    """
    if not isinstance(n, bytes):
        raise TypeError('expected bytes, not %s' % type(n).__name__)
    if len(n) not in (1, 2, 4, 8):
        raise TypeError('bytes must be 1, 2, 4, or 8 bytes in length')


def calcsize(fmt):
    """
    calcsize(fmt) -> int

    Return size of C struct described by format string fmt.
    See struct.__doc__ for more on format strings.
    """
    return struct.calcsize(fmt)


def pack(fmt, *args):
    """

