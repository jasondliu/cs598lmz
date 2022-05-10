import _struct
# Test _struct.Struct.

import struct
import sys

# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if expected != got:
        print('error in _struct.Struct: expected %d, got %d' % (expected, got))
        sys.exit(1)

test_struct('i', 4)
test_struct('ii', 8)
test_struct('iii', 12)
test_struct('iiii', 16)
test_struct('iiiii', 20)
test_struct('iiiiii', 24)
test_struct('iiiiiii', 28)
test_struct('iiiiiiii', 32)
test_struct('iiiiiiiii', 36)
test_struct('iiiiiiiiii', 40)
test_struct('iiiiiiiiiii', 44)
test_struct('iiiiiiiiiiii', 48)
test_struct('iiiiiiiiiiiii', 52)
test_struct('iiiiiiiiiiiiii', 56)
