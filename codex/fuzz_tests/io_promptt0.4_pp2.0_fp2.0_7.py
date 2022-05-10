import io
# Test io.RawIOBase

import _io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

try:
    import threading
except ImportError:
    threading = None

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')
        self.r = io.RawIOBase(self.f)

    def tearDown(self):
        self.r.close()
        self.f.close()
        unlink(TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readall)

    def test_write(self):
        self.assertRaises(io.Un
