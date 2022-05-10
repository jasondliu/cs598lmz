import _struct
# Test _struct.Struct
import os
import string
import sys
import unittest
from test import test_support
import test_struct

TESTFORMAT = 'hhhhhhhhhhhhhhhiillfffffffd'

class _MaxAlignTestCase(unittest.TestCase):
    # Make sure that the struct module keeps _struct.Struct aligned
    # with struct.Struct and struct.calcsize()
    # http://bugs.python.org/issue8045
    def testMaxAlign(self):
        self.assertEqual(struct.calcsize("@"), _struct.calcsize("@"))
        self.assertEqual(struct.calcsize("@P"), _struct.calcsize("@P"))
        self.assertEqual(struct.calcsize("@BHHHHH"), _struct.calcsize("@BHHHHH"))
        self.assertEqual(struct.calcsize("@QQQQQQQQ"), _struct.calcsize("@QQQQQQQQ"))
        self.assertEqual(struct.calcsize("=QQQ
