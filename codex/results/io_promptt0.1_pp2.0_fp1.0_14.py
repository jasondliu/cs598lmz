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

# Base class for testing a RawIOBase implementation
class BaseRawTests(object):
    # Subclass must define a RawIOBase implementation.
    io_class = None

    def setUp(self):
        self.f = self.io_class()
        self.f.__init__ = lambda *args: None

    def tearDown(self):
        self.f.close()
        self.f = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'mode'))
        self.assertTrue(hasattr(self.f, 'name'))
        self.assertTrue(hasattr(self.f, 'closed'))
        self.assertTrue(hasattr(self.f, 'close'))
        self.assertTrue(hasattr(self.f, 'fileno'))
        self.assertTrue(hasattr(self.f,
