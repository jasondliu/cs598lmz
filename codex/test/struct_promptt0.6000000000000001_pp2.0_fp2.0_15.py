import _struct
# Test _struct.Struct

import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            s = _struct.Struct()
        with self.assertRaises(TypeError):
            s = _struct.Struct(42)
        with self.assertRaises(TypeError):
            s = _struct.Struct('')
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.pack(42), b'*\x00\x00\x00')
        self.assertEqual(s.pack_into(bytearray(12), 3, 42), None)
