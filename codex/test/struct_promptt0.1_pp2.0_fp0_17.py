import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

class StructTestCase(unittest.TestCase):

    def test_struct_doc(self):
        self.assertEqual(_struct.Struct.__doc__,
                         "Compiled struct object")

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42, 42)
        with self.assertRaises(TypeError):
            _struct.Struct("hi")
        with self.assertRaises(TypeError):
            _struct.Struct("=hi")
        with self.assertRaises(TypeError):
            _struct.Struct("=b", "hi")
        with self.assertRaises(TypeError):
            _struct.Struct("=b", 42, 42)
        with self.assertRaises(TypeError):
            _struct.Struct("=b", 42, "hi")
