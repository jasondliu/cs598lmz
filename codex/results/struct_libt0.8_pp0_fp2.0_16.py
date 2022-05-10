import _struct
import types
import sys
import math
import zlib
from six import BytesIO as StringIO


def _pack(fmt, *args):
    # On 32-bit, packing a 64-bit int loses precision, so we have
    # to split it in two.
    if sys.maxsize < 2 ** 32 and fmt.endswith('Q'):
        high, low = divmod(args[-1], 2 ** 32)
        args = args[:-1] + (high, low)
    return _struct.pack('<' + fmt, *args)


def _isdict(x):
    return isinstance(x, dict)


def _isfloat(x):
    return isinstance(x, float)


def _isint(x):
    return isinstance(x, (int, long))


def _islist(x):
    return isinstance(x, (list, tuple))


def _isbytes(x):
    return isinstance(x, (bytes, bytearray))


def _isfile(x):
    return isinstance
