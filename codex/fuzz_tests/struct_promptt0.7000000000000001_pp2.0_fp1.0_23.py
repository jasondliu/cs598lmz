import _struct
# Test _struct.Struct subclasses

import unittest
import io
from test import support

class AllOtherSizeStruct(object):
    def __init__(self):
        self.format = 'i'
        self.size = 8

    def pack(self, *args):
        return _struct.Struct(self.format).pack(*args)

    def unpack(self, *args):
        return _struct.Struct(self.format).unpack(*args)

    def pack_into(self, *args):
        return _struct.Struct(self.format).pack_into(*args)

    def unpack_from(self, *args):
        return _struct.Struct(self.format).unpack_from(*args)

class TestStruct(unittest.TestCase):
    s = _struct.Struct('i')
    def test_constructor(self):
        self.assertEqual(self.s.format, 'i')
        self.assertEqual(self.s.size, _struct.calcsize('i'))
        self.assertRaises(TypeError, _struct.
