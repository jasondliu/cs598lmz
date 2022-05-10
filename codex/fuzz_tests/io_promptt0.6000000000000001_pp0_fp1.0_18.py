import io
# Test io.RawIOBase
#
# This test checks that RawIOBase is a working base class for raw I/O.
# It does not test the actual reading and writing of data.

import _io
import io
import os
import pickle
import sys
import unittest
from test import support
from test.support import bigmemtest

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO()
        self.r = io.RawIOBase(self.f)

    def tearDown(self):
        self.f.close()
        self.r.close()

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, b'')

    def test_write(self):
        self.assertRaises(io
