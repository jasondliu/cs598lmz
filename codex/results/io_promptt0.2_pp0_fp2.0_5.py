import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b"blah")

    def test_detach(self):
        self.assertRaises(io.UnsupportedOperation, self.f.detach)

    def test_seek(self):
        self.assertRa
