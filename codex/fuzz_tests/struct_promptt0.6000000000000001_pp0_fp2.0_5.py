import _struct
# Test _struct.Struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('hhi')
        with self.assertRaises(TypeError):
            _struct.Struct('hh', 42)

        s = _struct.Struct('hh')
        self.assertEqual(s.format, 'hh')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1, 2), b'\x01\x00\x02\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00'), (1, 2))
        with self.assertRaises(struct.error):
