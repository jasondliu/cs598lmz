import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the class attributes name and description.
class BaseRawIOSharingTests:

    def setUp(self):
        self.f = self.io.open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_weakref(self):
        p = weakref.proxy(self.f)
        self.assertEqual(p.read(0), b'')

    def test_read(self):
        self.f.write(b"abc")
        self.f.seek(0)
        self.assertEqual(self.f.read(0), b'')
        self.assertEqual(self.f.read(1), b
