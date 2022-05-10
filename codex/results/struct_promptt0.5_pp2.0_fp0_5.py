import _struct
# Test _struct.Struct
import unittest

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()

        with self.assertRaises(TypeError):
            _struct.Struct('')

        with self.assertRaises(TypeError):
            _struct.Struct('P')

        with self.assertRaises(TypeError):
            _struct.Struct('P', '')

        with self.assertRaises(TypeError):
            _struct.Struct('', 1)

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack_into(bytearray(), 0, 1), 4)

        with self.assertRaises(TypeError):
            _struct.Struct('P')

        with self.assertRaises(TypeError):
            _struct.Struct('P', 1
