import io
# Test io.RawIOBase with an io.BufferedIOBase that allows seeking.

import io
import io
import _pyio as pyio
import unittest
import weakref
import tempfile
import os

from test import test_support as support

TESTFN = support.TESTFN

class BufferedIOMixin(object):
    # Mixin defining tests common to RawIOBase and BufferedIOBase
    # (but not their subclasses)

    def test_close_detach(self):
        rawio = self.RawIOClass(self.MockRawIO())
        self.assertFalse(rawio.closed)
        self.assertIsNotNone(rawio.fileno())
        rawio.close()
        self.assertTrue(rawio.closed)
        self.assertRaises(ValueError, rawio.fileno)
        self.assertIsNone(rawio.close())
        self.assertIsNone(rawio.fileno())

    def test_read_non_blocking(self):
        # Make sure self.read() returns None or 0 in non-blocking mode.
