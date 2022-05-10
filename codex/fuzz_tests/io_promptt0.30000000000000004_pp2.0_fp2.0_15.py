import io
# Test io.RawIOBase

import io
import os
import tempfile
import unittest

from test import support

class RawIOBaseTestCase(unittest.TestCase):

    def test_read_non_blocking(self):
        # Issue #18808: RawIOBase.read() should return None on non-blocking
        # objects.
        class NonBlocking(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                return 0
        self.assertIsNone(NonBlocking().read(1))

    def test_read_into_non_blocking(self):
        # Issue #18808: RawIOBase.readinto() should return None on non-blocking
        # objects.
        class NonBlocking(io.RawIOBase):
            def readable(self):
                return True
            def read(self, n):
                return b""
        self.assertIsNone(NonBlocking().readinto(bytearray(1)))

    def test_read_write_closed(self):
        # Issue #18808: Raw
