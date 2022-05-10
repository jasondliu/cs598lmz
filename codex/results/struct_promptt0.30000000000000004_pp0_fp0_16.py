import _struct
# Test _struct.Struct.

import struct
import sys

def test(fmt, *args):
    print fmt, repr(args)
    s = _struct.Struct(fmt)
    print s.size, s.format
    print repr(s.pack(*args))
    print repr(s.unpack(s.pack(*args)))

test('i', 1)
test('ii', 1, 2)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)
test('i', 1)

