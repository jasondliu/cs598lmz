import io
# Test io.RawIOBase

import io
import os
import sys
import tempfile
import unittest
import weakref
import warnings

from test import test_support

try:
    import threading
except ImportError:
    threading = None

# A mixin defining tests common to RawIOBase and BufferedIOBase.
# The actual tests are defined in test_io.
class BaseIOTest:

    # Overridden in subclasses.
    io_mode = "r"
    io_mode_rw = "r+"
    io_mode_append = "a"
    io_mode_text = "rt"
    io_mode_text_rw = "r+t"
    io_mode_text_append = "at"

    def test_attributes(self):
        f = self.open(support.TESTFN, "w")
        try:
            self.assertEqual(f.mode, "w")
            self.assertEqual(f.name, support.TESTFN)
            self.assertTrue(f.closed)
        finally:
            f.
