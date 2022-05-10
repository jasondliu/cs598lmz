import _struct
# Test _struct.Struct

# XXXX this test needs to be completed

import _struct
import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test struct.pack and struct.unpack.
        # XXXX this test needs to be completed
        self.assertEqual(_struct.pack('i', 12345), b'\x39\x30\x00\x00')
        self.assertEqual(_struct.pack('i', 12345), b'\x39\x30\x00\x00')
        self.assertEqual(_struct.unpack('i', b'\x39\x30\x00\x00'), 12345)
        self.assertEqual(_struct.pack('i', -12345), b'\xc7\xcf\xff\xff')
        self.assertEqual(_struct.unpack('i', b'\xc7\xcf\xff\xff'), -12345)
