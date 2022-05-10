import _struct
# Test _struct.Struct()

import sys

def test_struct(fmt, x):
    s = _struct.Struct(fmt)
    got = s.pack(x)
    expected = struct.pack(fmt, x)
    if got != expected:
        print '%s: expected %r, got %r' % (fmt, expected, got)

def test_struct_unpack(fmt, x):
    s = _struct.Struct(fmt)
    got = s.unpack(s.pack(x))
    expected = (x,)
    if got != expected:
        print '%s: expected %r, got %r' % (fmt, expected, got)

def test_struct_unpack_iter(fmt, x):
    s = _struct.Struct(fmt)
    got = tuple(s.iter_unpack(s.pack(x)))
    expected = (x,)
    if got != expected:
        print '%s: expected %r, got %r' % (fmt, expected, got)

def test_struct_
