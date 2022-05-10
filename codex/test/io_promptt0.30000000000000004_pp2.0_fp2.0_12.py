import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIOTest:
    # Subclasses may override.
    filename = None
    def setUp(self):
        if self.filename is not None:
            try:
                os.unlink(self.filename)
            except OSError:
                pass

    def tearDown(self):
        if self.filename is not None:
            try:
                os.unlink(self.filename)
            except OSError:
                pass

    def test_read(self):
        self.assertEqual(self.read(0), b"")
        self.assertEqual(self.read(5), b"abcde")
        self.assertEqual(self.read(1), b"")
        self.assertEqual(self.read(0), b"")

