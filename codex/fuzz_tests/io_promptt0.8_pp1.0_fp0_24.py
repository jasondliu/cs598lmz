import io
# Test io.RawIOBase subclasses that are not file-like.
# Issue #21007: io.RawIOBase subclasses read(), readinto() and readall()
# should be allowed to return a short read.

import errno
import io
import os
import sys
import unittest
import unittest.mock
from test import support

from test.support import TESTFN, check_warnings

# Check that io.RawIOBase subclasses return short reads from read(), readinto()
# and readall()
class TestShortRead(unittest.TestCase):

    class FakeRawIO(io.RawIOBase):

        def read(self, size=-1):
            if size == -1:
                return b'blah'
            else:
                return b'blah'[:size]

        def readinto(self, b):
            b[:4] = b'blah'
            return 4

        def readall(self):
            return b'blah'

    def test_read(self):
        with TestShortRead.FakeRawIO() as f:
            self.
