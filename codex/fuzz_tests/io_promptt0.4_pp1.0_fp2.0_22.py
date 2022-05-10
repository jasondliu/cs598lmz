import io
# Test io.RawIOBase

import os
import sys
import unittest
from test import support

# The test_io test suite uses os.urandom() to generate random byte strings.
# This function is not available on all platforms, so we skip this test suite
# if it is not available.
try:
    os.urandom(1)
except NotImplementedError:
    raise unittest.SkipTest("os.urandom() not available")


class RawIOTest(unittest.TestCase):

    def test_read_write(self):
        # Test RawIOBase.read() and RawIOBase.write()
        for b in (b"", b"a", b"ab", b"abc", b"abcd", b"abcde", b"abcdef"):
            for n in range(1, len(b)):
                for bufsize in (1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 63, 64,
                                65, 100):
                    rawio = io.BytesIO(b)
                    self.assertEqual(
