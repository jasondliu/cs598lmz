import _struct
# Test _struct.Struct(format).pack_into(buffer, offset, v1, v2, ...)

import array
import sys
import unittest
from test import support

# Helper to create a buffer of the right size and type.
def create_buffer(size):
    if sys.byteorder == 'little':
        return array.array('b', b'\0' * size)
    else:
        return array.array('B', b'\0' * size)

class PackIntoTest(unittest.TestCase):

    def test_pack_into(self):
        # test pack_into with a variety of formats and offset values
        for format, values in [
            ('b', (-127, 0, 127)),
            ('B', (0, 127, 255)),
            ('h', (-32767, 0, 32767)),
            ('H', (0, 32767, 65535)),
            ('i', (-2147483647, 0, 2147483647)),
            ('I', (0, 2147483647, 4294967295)),
            ('l', (-2
