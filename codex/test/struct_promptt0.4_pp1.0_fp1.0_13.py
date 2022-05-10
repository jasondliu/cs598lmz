import _struct
# Test _struct.Struct.unpack_from.

import array
import sys

from test import support

# Issue #1602: unpack_from() segfaulted when the format string started
# with an empty repetition specifier.
def test_empty_repetition():
    s = _struct.Struct('xB')
    a = array.array('B', b'\x00\x01')
    s.unpack_from(a, 0)

def test_empty_string():
    s = _struct.Struct('')
    a = array.array('B', b'\x00\x01')
    s.unpack_from(a, 0)

def test_unpack_from():
    # Test the offset parameter of unpack_from().
    s = _struct.Struct('i')
    a = array.array('B', b'\x01\x02\x03\x04\x05\x06\x07\x08')
    # Offset 0.
    res = s.unpack_from(a, 0)
