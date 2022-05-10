import _struct
# Test _struct.Struct()
import struct
import sys
import unittest

class StructTest(unittest.TestCase):
    def test_word(self):
        # Size of the struct
        self.assertEqual(struct.calcsize('hhi'), _struct.Struct('hhi').size)
        # Access by name
        s = _struct.Struct('hhi')
        self.assertEqual(s.unpack_from(b'\x01\x00\x02\x00\x03\x00\x04\x00'),
            (1, 512, 67305985))
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x03\x00\x04\x00'),
            (1, 512, 67305985))
        # Access by index
        s = _struct.Struct('hhl')
