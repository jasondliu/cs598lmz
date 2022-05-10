import _struct
# Test _struct.Struct

# This test is not exhaustive.  It only tests the functionality
# that is needed by the marshal module.

import struct
import sys

if sys.byteorder == 'little':
    endianness = '<'
else:
    endianness = '>'

def test_format(format, value, expected):
    s = _struct.Struct(endianness + format)
    buf = s.pack(value)
    assert buf == expected
    assert s.unpack(buf) == (value,)

def test_int(format, value, expected):
    test_format(format, value, expected)
    test_format(format, -value, b'\0' * (len(expected) - 1) + b'\xff')

def test_int_overflow(format, value):
    s = _struct.Struct(endianness + format)
    try:
        s.pack(value)
    except OverflowError:
        pass
    else:
        assert False, "expected OverflowError"

def test_uint(format, value,
