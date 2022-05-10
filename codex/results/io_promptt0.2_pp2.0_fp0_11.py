import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class to provide tests common to RawIOBase and BufferedIOBase.
class BaseIOTest(object):
    # Subclasses should override.
    io_mode = None

    def setUp(self):
        self.f = open(TESTFN, self.io_mode)

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, self.io_mode)
        self.assertEqual(self.f.name, TESTFN)
        self.assertTrue(self.f.closed)

    def test_isatty(self):
        self.assertFalse(self.f.isatty())

    def test_tell(self):
        self.assertEqual(self.f.tell(), 0)

    def test_truncate(self
