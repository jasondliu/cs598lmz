import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
import errno

from test import support

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # Subclasses must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.b_prefix

    def setUp(self):
        self.f = self.io.open(self.filename, self.mode)

    def tearDown(self):
        if self.f:
            self.f.close()
        try:
            os.unlink(self.filename)
        except OSError:
            pass

    def test_attributes(self):
        self.assertEqual(self.f.mode, self.mode)
        self.assertEqual(self.f.name, self.filename)
        self.assertTrue(self.f.closed)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)
