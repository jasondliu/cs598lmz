import _struct
# Test _struct.Struct methods on a simple struct

from test.test_support import run_unittest, run_doctest, findfile
from test.test_support import import_module, bigaddrspacetest
from test.script_helper import assert_python_ok
import sys
import unittest
import os

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        import _struct
        s = _struct.Struct('h')
        self.assertEqual(s.unpack('\x00\x01'), (1,))
        self.assertEqual(s.unpack('\x00\x01'), (1,))
        self.assertRaises(TypeError, s.unpack)
        self.assertRaises(TypeError, s.unpack, 'hi')
        self.assertRaises(TypeError, s.unpack, 'hi', 'there')
        self.assertRaises(TypeError, s.unpack, 42)
        self.assertRaises(TypeError, s.unpack, buffer('\x00
