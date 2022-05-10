import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import import_helper
from test.support import requires

import os
import sys
import platform

# Skip tests if there is no C implementation
io = import_helper.import_module('io')

# Test RawIOBase using a StringIO object

# XXX more tests needed

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        self.r = io.BytesIO(b"1234567890")

    def test_read(self):
        self.assertEqual(self.r.read(4), b"1234")
        self.assertEqual(self.r.read(4), b"5678")
        self.assertEqual(self.r.read(4), b"90")
        self.assertRaises(TypeError, self.r.read, None)

    def test_readall(self):
        self.assertEqual(self.r.readall(), b"1234567890")
        self.assertRaises(ValueError
