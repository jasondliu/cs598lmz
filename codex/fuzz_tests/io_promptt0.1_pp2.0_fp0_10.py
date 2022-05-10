import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

# A mixin for RawIOBase tests that defines a few small read-write-seek
# files and a tearDown() method that closes them.
class RawIOMixin:
    def setUp(self):
        # We need a real file, not just a StringIO, for the tell() test.
        self.f = open(support.TESTFN, 'w+b')
        self.f.write(b'abcdefghijklmnopqrstuvwxyz')
        self.f.flush()
        self.f.seek(0, 0)
        self.f2 = open(support.TESTFN, 'w+b')
        self.f2.write(b'0123456789012345678901234567890123456789')
        self.f2.flush()
        self.f2.seek(0, 0)
        self.f3 = open(support.TESTFN, 'w+b')
        self
