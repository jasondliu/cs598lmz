import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno

from test import support

# A mixin for testing RawIOBase
class BaseRawIOMixin:

    # Subclasses must override
    def rawio(self, *args, **kwargs):
        raise NotImplementedError

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        raw = self.rawio()
        self.assertRaises(io.UnsupportedOperation, getattr, raw, 'name')
        self.assertRaises(io.UnsupportedOperation, getattr, raw, 'mode')
        self.assertRaises(io.UnsupportedOperation, getattr, raw, 'closed')
        raw.close()
        self.assertTrue(raw.closed)

    def test_read(self):
        raw = self.rawio()
        self.assertRaises(io.UnsupportedOperation, raw.read)
        raw.close
