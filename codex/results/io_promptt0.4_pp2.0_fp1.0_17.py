import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
from test import test_support
from test.test_support import TESTFN, run_unittest

# This test is intended to be run from the test directory, so the
# test data files are in the 'data' subdirectory.
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def open_data(filename):
    return open(os.path.join(DATA_DIR, filename), 'rb')

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        os.unlink(TESTFN)

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation
