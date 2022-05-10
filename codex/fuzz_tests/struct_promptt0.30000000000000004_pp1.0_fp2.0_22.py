import _struct
# Test _struct.Struct

# This is a list of (format, size, value, packed) tuples.
# The packed value is a sample; it need not match what Struct
# produces, but it must be the right size.

import sys

tests = [
    ('x', 1, 'x', 'x'),
    ('c', 1, 'x', 'x'),
    ('b', 1, 7, '\7'),
    ('B', 1, 7, '\7'),
    ('h', 2, 700, '\002\274'),
    ('H', 2, 700, '\002\274'),
    ('i', 4, sys.maxint, '\177\377\377\377'),
    ('I', 4, sys.maxint, '\177\377\377\377'),
    ('l', 4, sys.maxint, '\177\377\377\377'),
    ('L', 4, sys.maxint, '\177\377\377\377'),
    ('f', 4, 3.14, '@\070\245\360'),
    ('d', 8, 3.14
