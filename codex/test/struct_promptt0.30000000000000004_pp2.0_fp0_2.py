import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test the struct module.
        from _struct import calcsize, pack, unpack
        self.assertEqual(calcsize('i'), 4)
        self.assertEqual(calcsize('i4s'), 8)
        self.assertEqual(calcsize('i4sh'), 12)
        self.assertEqual(calcsize('i4shl'), 16)
        self.assertEqual(calcsize('i4shL'), 16)
        self.assertEqual(calcsize('i4shlq'), 24)
        self.assertEqual(calcsize('i4shLq'), 24)
        self.assertEqual(calcsize('i4shlQ'), 24)
        self.assertEqual(calcsize('i4shLQ'), 24)
        self.assertEqual(calcsize('i4shf'), 12)
