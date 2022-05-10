import _struct
# Test _struct.Struct
import sys
import mmap
import os
import cStringIO
import struct
import unittest
import tempfile
import sys

class StructTestCase(unittest.TestCase):

    def test_format(self):
        # Check that the constructor accepts format strings correctly
        s = _struct.Struct('hhl')
        self.assertEqual(s.size, _struct.calcsize('hhl'))
        s = _struct.Struct('hhh')
        self.assertEqual(s.size, _struct.calcsize('hhh'))

        # Check that the constructor rejects bad format strings
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, 'cc', 'sss')

        # Check that the format string is saved correctly
        s = _struct.Struct('hcx')
        self.assertEqual(s.format, 'hcx')

        # Check that size is calculated correctly
        self.assertE
