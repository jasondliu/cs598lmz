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
from test.support import TESTFN, unlink, run_unittest

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the class attributes name and description.
class BaseRawIO(object):
    name = None
    description = None

    def setUp(self):
        self.f = self.open()

    def tearDown(self):
        self.f.close()

    def open(self):
        raise NotImplementedError

    def test_read(self):
        self.assertEqual(self.f.read(0), b'')
        self.assertEqual(self.f.read(1), self.read(0, 1))
        self.assertEqual(self.f.read(10), self.read(0, 10))
        self.assertEqual(self.f.read(100), self
