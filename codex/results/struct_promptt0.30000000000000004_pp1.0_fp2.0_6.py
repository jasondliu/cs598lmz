import _struct
# Test _struct.Struct

import struct
import sys
import unittest

from test import test_support

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('ii'), _struct.calcsize('ii'))
        self.assertEqual(struct.calcsize('i'*100), _struct.calcsize('i'*100))
        self.assertEqual(struct.calcsize('i'*1000), _struct.calcsize('i'*1000))
        self.assertEqual(struct.calcsize('i'*10000), _struct.calcsize('i'*10000))
        self.assertEqual(struct.calcsize('i'*100000), _struct.calcsize('i'*100000))

        fmt = 'i'*100000
        s = _struct.Struct(fmt)
        self.assertEqual(s.size, struct.
