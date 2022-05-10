import io
# Test io.RawIOBase
#
# Test the implementation of io.RawIOBase.
#
# This test checks the RawIOBase implementation against the stdlib
# io.RawIOBase implementation.

import _io
import unittest
import unittest.mock

from test import support

# A mixin class with common tests for RawIOBase objects
class CommonRawTests(object):
    def test_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(5), self.data[:5])
        self.assertEqual(self.io.read(5), self.data[5:10])
        self.assertEqual(self.io.read(1000), self.data[10:])
        self.assertEqual(self.io.read(1000), b'')

    def test_readall(self):
        self.assertEqual(self.io.readall(), self.data)
        self.assertEqual(self.io.readall(), b'')

    def test
