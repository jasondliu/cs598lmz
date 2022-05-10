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

# A mixin for testing RawIOBase objects.
#
# Subclasses must define read(), readall() and write() methods.
class BaseTestRawIO(object):
    # Subclasses may override.
    def new_instance(self):
        return self.io.BytesIO()

    def setUp(self):
        self.io = support.import_module(self.io_module)
        self.r = self.new_instance()

    def tearDown(self):
        self.r.close()
        self.r = None

    def test_attributes(self):
        self.assertEqual(self.r.mode, "wb+")
        self.assertEqual(self.r.name, None)
        self.assertEqual(self.r.closed, False)
        self.assertEqual(self.r.isatty(), False)
        self.assertEqual(
