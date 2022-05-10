import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Helper for testing readinto()
def readinto_helper(self, source, length, buffer):
    source.seek(0)
    self.assertEqual(source.readinto(buffer), length)
    self.assertEqual(buffer[:length], source.read())

class TestRawIOBase(unittest.TestCase):
    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def test_readinto(self):
        self.f.write(b'abcdefghijklmnop')
        self.f.flush()
        readinto_helper(self, self.f, 16, bytearray(b'x' * 16))
        readinto_helper(self, self
