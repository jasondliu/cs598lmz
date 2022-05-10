import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

from test import support

# Base class for testing RawIOBase
class BaseTestRawIO(object):
    # Subclass must define a read() method.
    # It may also define setUp(), tearDown(), and __init__().

    def test_read(self):
        # Read at various positions to test seeking behaviour.
        for i in range(len(self.data)):
            b = self.read(1, i)
            self.assertEqual(len(b), 1)
            self.assertEqual(b, self.data[i:i+1])

        # Read various lengths
        for i in range(len(self.data)):
            b = self.read(i)
            self.assertEqual(len(b), i)
            self.assertEqual(b, self.data[:i])

        # Read zero bytes
        b = self.read(0)
        self.assertEqual(len(b), 0)


