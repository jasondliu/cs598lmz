import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import random
import warnings
import functools
import contextlib

from test import support
from test.support import TESTFN, unlink, run_with_locale, check_warnings

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # Subclasses should override.
    def setUp(self):
        self.filename = TESTFN

    def tearDown(self):
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def test_attributes(self):
        # test RawIOBase attributes
        f = self.open(self.filename, "w+")
        self.assertEqual(f.mode, "w+")
        if hasattr(os, "fspath"):
            self.assertEqual(os.fspath(f), self.filename)
        f.close()

    def test_read(self):
        # test RawIOBase read()
        f
