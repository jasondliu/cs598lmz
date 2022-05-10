import _struct
# Test _struct.Struct
#
# The code for this test was derived from Lib/test/test_struct.py

import sys
import unittest
import warnings

from test.support import run_unittest, check_impl_detail, TESTFN, unlink

class StructTestCase(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('=i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('<i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('>i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('!i'))

    def test_native_sizes(self):
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('@i'))
        self.assertEqual(_struct.calcsize('i'), _struct.calcsize('=i'))

   
