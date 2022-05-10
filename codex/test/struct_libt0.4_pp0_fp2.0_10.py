import _struct

from . import _compat
from . import _util

_int_types = (int, _compat.long)


def _read_exactly(f, n):
    """Read n bytes from f, raising an exception if it fails."""
    buf = f.read(n)
    if len(buf) != n:
        raise EOFError("%d bytes requested, but only %d bytes read" %
                       (n, len(buf)))
    return buf


def _read_until_null(f):
    """Read bytes from f until a null byte is encountered."""
    buf = bytearray()
    while True:
        b = f.read(1)
        if not b:
            raise EOFError("unexpected EOF while reading null-terminated string")
        if b == b'\x00':
            return bytes(buf)
        buf.extend(b)


def _read_struct(f, fmt):
    """Read a struct from f, raising an exception if it fails."""
    size = _struct.calcsize
