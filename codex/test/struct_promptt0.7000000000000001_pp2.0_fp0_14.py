import _struct
# Test _struct.Struct.__new__
import unittest

class StructTest(unittest.TestCase):
    def test_new(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(1)
        with self.assertRaises(TypeError):
            _struct.Struct('test')
        with self.assertRaises(TypeError):
            _struct.Struct('test', 1)
        with self.assertRaises(TypeError):
            _struct.Struct('test', 0)
        with self.assertRaises(TypeError):
            _struct.Struct('test', 1, 1)
        with self.assertRaises(TypeError):
            _struct.Struct('test', 0, 1)
        with self.assertRaises(TypeError):
            _struct.Struct('test', 1, 1, 1)
        with self.assertRaises(TypeError):
            _struct.Struct('test', 0, 1, 1)
