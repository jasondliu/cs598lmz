import _struct
# Test _struct.Struct.__repr__.

from test.test_support import run_unittest
from test.test_support import verbose

import _struct
from _struct import Struct

class StructTest(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Struct("i")), "Struct('i')")
        self.assertEqual(repr(Struct("<i")), "Struct('<i')")
        self.assertEqual(repr(Struct("ii")), "Struct('ii')")
        self.assertEqual(repr(Struct("")), "Struct('')")
        self.assertEqual(repr(Struct("b")), "Struct('b')")
        self.assertEqual(repr(Struct("bx")), "Struct('bx')")
        self.assertEqual(repr(Struct("cb")), "Struct('cb')")
        self.assertEqual(repr(Struct("cbx")), "Struct('cbx')")
