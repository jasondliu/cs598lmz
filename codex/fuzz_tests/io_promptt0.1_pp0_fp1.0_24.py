import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys

from test import support

# A mixin for RawIOBase tests that defines a few small read-write-seek
# files and a tearDown() method to close them.
class RawIOMixin:
    def setUp(self):
        self.files = [self.open(support.TESTFN, 'w+b') for x in range(3)]
        for f in self.files:
            self.addCleanup(f.close)
        self.files[0].write(b"abc")
        self.files[1].write(b"defghi")
        self.files[2].write(b"jklmnopqrstuvwxyz")

    def tearDown(self):
        for f in self.files:
            f.close()
        for f in self.files:
            support.unlink(f.name)

class RawIOBaseTest(RawIOMixin, unittest.TestCase):
    def test_constructor(self):

