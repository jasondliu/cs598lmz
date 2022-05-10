import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _pyio as pyio

from test import support

# Base class for testing a RawIOBase implementation.
# To test a concrete RawIOBase implementation, subclass this and override
# setUp(), tearDown(), and possibly test names starting with "test_".
# setUp() should create self.r, the RawIOBase object to test.
# tearDown() should delete it.
class BaseRawTests:

    # Subclasses can override.
    def setUp(self):
        self.r = None

    def tearDown(self):
        if self.r is not None:
            self.r.close()
        self.r = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.r, "mode"))
        self.assertTrue(hasattr(self.r, "name"))
        self.assertTrue(hasattr(self.r, "closed"))
        self.assertTrue(hasattr(self.r, "close
