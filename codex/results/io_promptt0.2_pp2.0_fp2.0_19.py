import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import TESTFN, run_unittest

import io
import os
import sys
import tempfile
import time
import errno

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        os.remove(TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b"blah")

    def test_close(self):
        self.f.close()
        self.assertTrue(self.f.closed)
        self.assertRaises
