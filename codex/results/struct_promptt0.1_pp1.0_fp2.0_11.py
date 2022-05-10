import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import _struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('ii'), _struct.calcsize('ii'))
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('ii'), _struct.calcsize('ii'))
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('ii'), _struct.calcsize('ii'))
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('ii'), _struct.calcsize('ii'))
       
