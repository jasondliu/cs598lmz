import _struct
# Test _struct.Struct

import unittest
import struct
from test import support
from test.support import bigmemtest

class StructTestCase(unittest.TestCase):

    def test_constructor(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '', '')

    def test_unpack(self):
        with self.assertRaises(TypeError):
            _struct.Struct('x').unpack()
        with self.assertRaises(TypeError):
            _struct.Struct('x').unpack(b'')
        with self.assertRaises(TypeError):
            _struct.Struct('x').unpack(b'', '', '')
        with self.assertRaises(struct.error):
            _struct.Struct('x').unpack(b'')
        with self.assertRaises(struct.error):
            _struct.Struct('x').unpack(b'x')
