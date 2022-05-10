import _struct
# Test _struct.Struct
#
# This tests the _struct module by making sure that the Struct object's
# pack and unpack methods work correctly.

import sys, unittest
from test import test_support

class StructTest(unittest.TestCase):
    def test_struct(self):
        import _struct

        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('i4s'), 8)
        self.assertEqual(_struct.calcsize('4si'), 8)
        self.assertEqual(_struct.calcsize('4si4s'), 12)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('ff'), 8)

        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), '\x00\x00\x00\x01')
        self.assertEqual(s.pack(0xffffffff), '\
