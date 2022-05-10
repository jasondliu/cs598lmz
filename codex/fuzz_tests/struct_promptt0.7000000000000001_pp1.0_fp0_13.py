import _struct
# Test _struct.Struct
from test.support import bigaddrspacetest
from test import support
import unittest
import sys
from test.support import run_unittest
from test.support.script_helper import assert_python_ok


class _TestStruct(unittest.TestCase):

    def test_bool(self):
        self.assertRaises(TypeError, _struct.Struct, '?')

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct, b'x')
        self.assertRaises(TypeError, _struct.Struct, 'x', b'')
        self.assertRaises(TypeError, _struct.Struct, 'x', '')
        self.assertRaises(TypeError, _struct.Struct, 'x', 'y')
        self.assertRaises(TypeError, _struct.Struct, 'x', '@')
        self.assertRaises(TypeError, _struct.Struct, 'x', '@y')
        self.assertRaises(TypeError, _struct.Struct, 'x', '@@')
       
