import _struct
# Test _struct.Struct.

import sys
import test
from test import test_support
from test.test_support import verbose, cpython_only, \
                              import_module, run_unittest, \
                              swap_attr
import unittest
from cStringIO import StringIO
import binascii
import array
from array import array
from random import random


class StructTestCase(unittest.TestCase):

    def setUp(self):
        self.fmt = 'hhl'
        self.s = _struct.Struct(self.fmt)
        self.data = array('b', '\0' * self.s.size)
        self.values = (1, -2, 3)

    def tearDown(self):
        pass

##    def test_unpack(self):
##        for v in self.values:
##            data = self.data
##            if len(data) > 8:
##                d1 = data[:8]
##                d2 = data[8:]
##                self.assertEqual(self.s.unpack
