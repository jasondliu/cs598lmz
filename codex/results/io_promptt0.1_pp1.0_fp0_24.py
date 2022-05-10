import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _io

from test import support

# Base class for testing io.RawIOBase.
# The tests are performed both in blocking and non-blocking mode.
#
# Subclasses must override the read, write and seek methods.
class RawIOTest:

    # Subclass must override
    read_mode = ""
    write_mode = ""

    def setUp(self):
        self.f = self.io.open(support.TESTFN, self.write_mode,
                              buffering=0)

    def tearDown(self):
        if not self.f.closed:
            self.f.close()
        support.unlink(support.TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, self.write_mode)
        self.assertEqual(self.f.name, support.TESTFN)
        self.assertEqual(self.f.closed, False)
        self.assert
