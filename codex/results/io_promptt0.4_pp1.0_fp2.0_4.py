import io
# Test io.RawIOBase

import io
import os
import sys
import tempfile
import unittest
from test import support

# Issue #18793: Check that io.RawIOBase.readinto() returns None
# when called with a 0-length buffer.
class RawIOBaseTest(unittest.TestCase):
    def test_readinto_zero_length(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, buf):
                return None
        with TestRawIO() as f:
            self.assertIsNone(f.readinto(bytearray(0)))

# Issue #19076: Check that io.RawIOBase.readinto() returns None
# when called with a 0-length buffer.
class RawIOBaseTest(unittest.TestCase):
    def test_readinto_zero_length(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, buf):
                return None
        with TestRawIO() as f:
            self.assertIsNone(f.readinto(bytear
