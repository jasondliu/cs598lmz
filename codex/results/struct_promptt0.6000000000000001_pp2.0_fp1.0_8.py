import _struct
# Test _struct.Struct

import unittest
from test import support

# The size and alignment of these types should be checked before
# running the other tests, as they are used to build the test
# patterns.

import sys

def check(typecode, size, alignment):
    assert _struct.calcsize(typecode) == size
    assert _struct.calcsize('=' + typecode) == size
    assert _struct.Struct(typecode).size == size
    assert _struct.Struct('=' + typecode).size == size
    assert _struct.Struct(typecode).alignment == alignment
    assert _struct.Struct('=' + typecode).alignment == alignment

def check_sizeof(typecode, size):
    try:
        import array
    except ImportError:
        pass
    else:
        assert array.array(typecode).itemsize == size

def check_range(typecode, min, max):
    try:
        import array
    except ImportError:
        pass
    else:
        a = array.array(typecode)
        a.append(min)
