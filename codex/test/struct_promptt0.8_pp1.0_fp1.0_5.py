import _struct
# Test _struct.Struct. The Struct class is a helper class to build
# common Structs in a simpler way.
from _testcapi import type_checks
import re
# Test that the sre module is not imported.
# XXX This should be removed after 2.3.
class TestSimpleTypes(unittest.TestCase):

    def test_frozenset(self):
        self.assertEqual(type(frozenset()), type(set()))
        self.assertEqual(frozenset([1, 2, 3]), frozenset((1, 2, 3)))

    def test_struct(self):
        # Test the Struct class.  This is a helper class to build common
        # Structs in a simpler way.
        # XXX This should be expanded.
        s = _struct.Struct(">h")
        self.assertEqual(s.size, 2)
        self.assertEqual(s.pack(1), b'\x00\x01')
        self.assertEqual(s.unpack(b'\x00\x01')[0], 1)
        self
