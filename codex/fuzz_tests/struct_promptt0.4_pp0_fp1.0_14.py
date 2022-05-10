import _struct
# Test _struct.Struct
# Test that we can create a Struct object with a format string,
# and that we can use it to convert between strings and tuples.

# Test that we can create a Struct object with a format string,
# and that we can use it to convert between strings and tuples.
import _struct
import sys

def test_basic():
    fmt = 'hhl'
    s = _struct.Struct(fmt)
    data = s.pack(1, 2, 3)
    print(repr(data))
    print(s.unpack(data))

def test_unpack_from():
    fmt = 'hhl'
    s = _struct.Struct(fmt)
    data = s.pack(1, 2, 3)
    print(repr(data))
    print(s.unpack_from(data))

def test_unpack_from_buffer():
    fmt = 'hhl'
    s = _struct.Struct(fmt)
    data = s.pack(1, 2, 3)
    print(repr(data))
    print(
