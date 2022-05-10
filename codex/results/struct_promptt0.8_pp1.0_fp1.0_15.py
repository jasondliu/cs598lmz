import _struct
# Test _struct.Struct for correct spec parameter handling
# Issue: http://bugs.python.org/issue7930

import sys, struct

# Test size calculation
if sys.byteorder == 'little':
    endianness = '<'
    expected_size = 2
else:
    endianness = '>'
    if sys.platform.startswith('win'):
        expected_size = 6
    else:
        expected_size = 8

s = _struct.Struct(endianness + "hi")

if s.size != expected_size:
    print("size: expected: %s got %s" % (expected_size, s.size))

# Test pack_into() for correct spec parameter handling
# Issue: http://bugs.python.org/issue8237
s = _struct.Struct(endianness + "i")

buf = bytearray(4)
s.pack_into(buf, 0, 42)
if sys.byteorder == 'little':
    expected = b'*\x00\x00\x00'
else:
    expected = b'
