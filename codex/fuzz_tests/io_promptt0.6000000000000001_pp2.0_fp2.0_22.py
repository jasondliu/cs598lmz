import io
# Test io.RawIOBase

import sys
import unittest
import weakref
import os
import io
import _io
import errno
import tempfile
import pickle
import gc
import contextlib
import shutil
import subprocess

from test.support import run_unittest, TESTFN, unlink, check_warnings
from test.support import import_fresh_module, cpython_only

try:
    import threading
except ImportError:
    threading = None

# A mixin for testing concrete RawIOBase implementations
class RawIOMixin:

    # Subclasses should override
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_attributes(self):
        rawio = self.RawIO()
        self.assertEqual(rawio.mode, '')
        self.assertFalse(rawio.readable())
        self.assertFalse(rawio.writable())
        self.assertFalse(rawio.seekable())
        self.assertEqual(rawio.readable(), rawio.isatty())
       
