import _struct
# Test _struct.Struct
#
# This test is based on the Python test_struct.py test, but it has been
# modified to use the _struct module, and to test only the little-endian
# format.
#
# This test is in the public domain.

import sys
import unittest

from test.support import run_unittest

class StructTestCase(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iI'), 8)
        self.assertEqual(_struct.calcsize('hi'), 4)
        self.assertEqual(_struct.calcsize('hhi'), 4)
        self.assertEqual(_struct.calcsize('hhhhi'), 6)
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('bb'), 2)
