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
from test.support import import_module

# Base class for testing a RawIOBase implementation.
# The class to be tested is given as the 'io' class attribute.
#
# Subclasses must override read(), seek(), and write().
#
# The setUp() method creates an instance self.io.
#
# If a subclass defines a tearDown() method, the io attribute will
# be None when tearDown() is called.
class RawIOTest(unittest.TestCase):

    io = None

    def setUp(self):
        self.io = self.io()

    def tearDown(self):
        io = self.io
        self.io = None
        if io is not None:
            io.close()

    def test_attributes(self):
        self.assertTrue(hasattr(self.io, 'mode'),
                        'io object has no attribute "mode"')
        self
