import _struct
# Test _struct.Struct
# struct
import struct
import unittest
from test import support
# The size of these formats should be known in advance.
# They should all be native byte order, since we want to know the size.
fixed_length_formats = [
    ('x', 0), ('c', 1), ('b', 1), ('B', 1), ('?', 1), ('h', 2), ('H', 2),
    ('i', 4), ('I', 4), ('l', 4), ('L', 4), ('q', 8), ('Q', 8), ('f', 4),
    ('d', 8)]
# These formats should also have a fixed size, but they can be different
# sizes in different architectures.
sizeof_short = struct.calcsize('=h')
sizeof_int = struct.calcsize('=i')
sizeof_long = struct.calcsize('=l')
sizeof_void_p = struct.calcsize('=P')
sizeof_float = struct.calcsize('=f')
sizeof_double = struct.calcsize('=d')
fixed_length
