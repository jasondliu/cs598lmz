import _struct

from . import lib
from . import py_compat
from . import pycompat
from . import util

# a list of hex-encoded hashes (and their aliases) that are not used
# in the DAG. This is used to detect hash collisions.
_nullhashes = set(b'0000000000000000000000000000000000000000')
# also consider nullid (all-zeros) as a null hash
_nullhashes.add(b'\0' * 20)


def int_from_hexstr(s):
    """Convert a string of hex digits to an integer."""
    return int(s, 16)


def hex(number):
    """Convert an integer or long to a lowercase hex string.

    >>> hex(10)
    'a'
    >>> hex(1000000000)
    '3b9aca00'
    """
    if not isinstance(number, pycompat.inttypes):
        number = int(number)
    if number < 0:
        # two's complement
        number += 1 << 32
    return '%x' % number


def
