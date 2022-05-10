import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation
class BaseTestRawIO(object):
    # Subclass must define a read() and write() method.
    # It may also define a seek(), tell(), truncate(),
    # and flush() method.

    def test_read(self):
        # Read a number of bytes
        self.assertEqual(self.read(0), b'')
        self.assertEqual(self.read(5), b'12345')
        self.assertEqual(self.read(5), b'67890')
        self.assertEqual(self.read(5), b'abcde')
        self.assertEqual(self.read(5), b'fghij')
        self.assertEqual(self.read(5), b'klmno')
        self.assertEqual(self.read(5), b'pqrst')
        self.assertEqual(self.read(5
