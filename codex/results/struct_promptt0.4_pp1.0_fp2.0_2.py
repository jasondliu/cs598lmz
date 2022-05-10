import _struct
# Test _struct.Struct

import struct
import sys
import unittest

from test import support

# The following is a list of (format, size, value) tuples.
# The value is what a native format would return.
# The size is in bytes.

format_data = [
    ('x', 1, '\x00'),
    ('c', 1, '\x38'),
    ('b', 1, '\x7f'),
    ('B', 1, '\xff'),
    ('?', 1, '\x01'),
    ('h', 2, '\x7fff'),
    ('H', 2, '\xffff'),
    ('i', 4, '\x7fffffff'),
    ('I', 4, '\xffffffff'),
    ('l', 4, '\x7fffffff'),
    ('L', 4, '\xffffffff'),
    ('q', 8, '\x7fffffffffffffff'),
    ('Q', 8, '\xffffffffffffffff'),
    ('f', 4, '\x00\x00\x80?'),
    ('
