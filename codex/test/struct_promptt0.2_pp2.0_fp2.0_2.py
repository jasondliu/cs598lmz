import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
import _testcapi

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('i4s'), _struct.calcsize('i4s'))
        self.assertEqual(struct.calcsize('i4sh'), _struct.calcsize('i4sh'))
        self.assertEqual(struct.calcsize('i4shh'), _struct.calcsize('i4shh'))
        self.assertEqual(struct.calcsize('i4shhi'), _struct.calcsize('i4shhi'))
        self.assertEqual(struct.calcsize('i4shhil'), _struct.calcsize('i4shhil'))
