import _struct
# Test _struct.Struct.
import struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # struct.unpack()
        self.assertEqual(_struct.unpack('hhl', b'\x01\x00\x02\x00\x03\x00\x00\x00'),
                         (1, 2, 3))
        self.assertEqual(_struct.unpack('hhl', bytearray(b'\x01\x00\x02\x00\x03\x00\x00\x00')),
                         (1, 2, 3))
        self.assertEqual(_struct.unpack('hhl', memoryview(b'\x01\x00\x02\x00\x03\x00\x00\x00')),
                         (1, 2, 3))
