import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #1702
        s = _struct.Struct('?')
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pack(False), b'\0')
        self.assertEqual(s.pack(True), b'\1')
        self.assertEqual(s.unpack(b'\0'), (False,))
        self.assertEqual(s.unpack(b'\1'), (True,))
        self.assertRaises(struct.error, s.pack, 2)
        self.assertRaises(struct.error, s.unpack, b'\2')

    def test_struct_bool_big_endian(self):
        # Issue #1702
        s = _struct.Struct('>?')
        self.assertEqual(s.size, 1)
