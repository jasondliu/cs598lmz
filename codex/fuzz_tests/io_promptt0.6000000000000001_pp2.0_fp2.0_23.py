import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import warnings
from test import test_support
from test.test_support import TESTFN, run_unittest

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        os.remove(TESTFN)

    def test_incomplete(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        self.assert_(hasattr(self.f, 'mode'), "I/O object should have mode attribute")
        self.assert_(hasattr(self.f, 'name'), "I/O object should have name attribute")
        self.assert_(hasattr(self.f, 'errors'), "I/O object should have errors attribute")
        self.assert_(hasattr(self.f, 'encoding'), "I/O object should have encoding attribute")

