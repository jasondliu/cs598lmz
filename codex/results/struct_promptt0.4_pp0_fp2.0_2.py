import _struct
# Test _struct.Struct

import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('hhi')
        self.assertEqual(s.size, 6)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00'),
                         (1, 512, 3))
        self.assertEqual(s.unpack_from(b'\xff\xfe\xfd\xfc\xfb\x00\x01\x00'),
                         (65534, 1))
        self.assertRaises(TypeError, s.pack, 1, 2, 3, 4)
        self.assertRaises(Type
