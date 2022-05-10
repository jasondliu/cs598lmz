import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings

from test import support
from test.support import os_helper

# Base class for testing a RawIOBase implementation.
# Subclasses must override read, readinto and seek.
class BaseRawIOBaseTests(object):
    # Subclass is expected to override.
    def setUp(self):
        self.rawio = self.io.open(self.TESTFN, "w+b")

    def tearDown(self):
        if self.rawio:
            self.rawio.close()
        support.unlink(self.TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(self.rawio, "mode"))
        self.assertTrue(hasattr(self.rawio, "name"))
        self.assertTrue(hasattr(self.rawio, "closed"))

    def test_read(self):
        self.rawio.write(b"abc")
        self.rawio.seek(0
