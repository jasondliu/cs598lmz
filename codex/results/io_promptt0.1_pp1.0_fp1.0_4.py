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
class BaseRawIOSharingTests(object):
    # Subclasses may override.
    name = 'BaseRawIO'
    description = 'Base class for RawIO tests'

    def setUp(self):
        self.f = self.io.open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_closed(self):
        self.assertFalse(self.f.closed)
        self.f.close()
        self.assertTrue(self.f.closed)

    def test_readable(self):
        self.assertTrue
