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
from test.support import TESTFN, unlink

# Base class for testing a RawIO implementation.
# Subclasses must override read(), readall() and seek(),
# and set the class attributes name, type2test and template.
class BaseRawIOSharingTests:
    # Subclasses can override to use a different type to test.
    type2test = None

    def setUp(self):
        # Create a test file
        f = open(TESTFN, 'wb')
        f.write(self.template)
        f.close()
        self.f = open(TESTFN, 'rb')

    def tearDown(self):
        self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        rawio = self.type2test(self.f)
        self.assertEqual(rawio.mode, 'rb')
        self.assert
