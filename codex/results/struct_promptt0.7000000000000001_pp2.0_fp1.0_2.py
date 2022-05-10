import _struct
# Test _struct.Struct.

import struct
import sys
from test import support

# A list of (format, size) pairs.
struct_test_cases = [
    ('x', 1),
    ('c', 1),
    ('b', 1),
    ('B', 1),
    ('?', 1),
    ('h', 2),
    ('H', 2),
    ('i', 4),
    ('I', 4),
    ('l', 4),
    ('L', 4),
    ('q', 8),
    ('Q', 8),
    ('f', 4),
    ('d', 8),
    ('s', 1),
    ('p', 1),
    ('P', 4),
]

def test_basics():
    for format, size in struct_test_cases:
        st = _struct.Struct(format)
        s = struct.Struct(format)

        # __doc__
        if st.__doc__ != s.__doc__:
            print(format, st.__doc__, s.__doc__)
        # __repr__
        if st.__
