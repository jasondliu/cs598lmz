import io
# Test io.RawIOBase

import _io
import io
import os
import pickle
import sys
import tempfile
import unittest
from test import support
from test.support import bigmemtest, bigaddrspacetest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing io.RawIOBase

class BaseRawIOBaseTests(object):

    def test_attributes(self):
        rawio = self.RawIO()
        self.assertFalse(rawio.readable())
        self.assertFalse(rawio.writable())
        self.assertFalse(rawio.seekable())
        self.assertRaises(io.UnsupportedOperation, rawio.fileno)
        self.assertRaises(io.UnsupportedOperation, rawio.isatty)
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, b'')
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self
