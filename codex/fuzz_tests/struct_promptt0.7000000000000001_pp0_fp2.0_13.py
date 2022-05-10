import _struct
# Test _struct.Struct

# Test some basic features of _struct.Struct.

import _struct
import sys


def test_basics():
    with _struct.Struct('xx') as s:
        if s.size != 2:
            raise ValueError('s.size returned %d, expected 2' % s.size)
        if len(s.pack(1)) != 2:
            raise ValueError('len(s.pack(1)) returned %d, expected 2' % len(s.pack(1)))
        if s.unpack(s.pack(1))[0] != 1:
            raise ValueError('s.unpack(s.pack(1))[0] returned %d, expected 1' % s.unpack(s.pack(1))[0])


def test_int_format():
    # This produces a struct.error:
    #    with _struct.Struct('q') as s: pass
    with _struct.Struct('i') as s:
        if s.size != 4:
            raise ValueError('s.size returned %d, expected 4' % s.size)
