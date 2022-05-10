import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #1702
        self.assertEqual(_struct.Struct('?').pack(True), b'\x01')
        self.assertEqual(_struct.Struct('?').pack(False), b'\x00')
        self.assertEqual(_struct.Struct('?').unpack(b'\x01'), (True,))
        self.assertEqual(_struct.Struct('?').unpack(b'\x00'), (False,))

    def test_struct_bool_error(self):
        # Issue #1702
        with self.assertRaises(TypeError):
            _struct.Struct('?').pack(1)
        with self.assertRaises(TypeError):
            _struct.Struct('?').pack(0)
        with self.assertRaises(TypeError):
            _struct.Struct('?').pack(1.0)
        with self.assertRaises(TypeError):
           
