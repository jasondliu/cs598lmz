import _struct
# Test _struct.Struct class

import unittest


class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()

        with self.assertRaises(TypeError):
            _struct.Struct(42)

        with self.assertRaises(TypeError):
            _struct.Struct('')

        with self.assertRaises(TypeError):
            _struct.Struct('P')

        with self.assertRaises(TypeError):
            _struct.Struct(b'P')

        with self.assertRaises(TypeError):
            _struct.Struct('P', 42)

        with self.assertRaises(TypeError):
            _struct.Struct('P', '')

        with self.assertRaises(TypeError):
            _struct.Struct('P', b'')

        with self.assertRaises(TypeError):
            _struct.Struct('P', 'café')

