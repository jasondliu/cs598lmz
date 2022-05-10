import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

# These tests test the raw I/O interface of the io module.
# They are intended to be run with a variety of raw I/O implementations,
# including read(), readinto() and readv() based versions, to ensure
# that the high-level I/O classes do the right thing.

# The tests are run with a RawIOBase implementation passed in as the
# constructor to the test cases.

class RawIOTest:

    # Subclass must override
    def setUp(self):
        raise NotImplementedError

    # Subclass must override
    def tearDown(self):
        raise NotImplementedError

    def test_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(1), b'x')
        self.assertEqual(self.io.read(1), b'y')
        self.assertEqual(self.io
