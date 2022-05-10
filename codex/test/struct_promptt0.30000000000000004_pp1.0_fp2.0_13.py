import _struct
# Test _struct.Struct.

import struct
import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(struct.calcsize('i'), _struct.Struct('i').size)
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.pack('i', 1), _struct.Struct('i').pack(1))
        self.assertEqual(struct.pack('i', 1), _struct.pack('i', 1))
        self.assertEqual(struct.unpack('i', b'\x01\x00\x00\x00')[0],
                         _struct.Struct('i').unpack(b'\x01\x00\x00\x00')[0])
