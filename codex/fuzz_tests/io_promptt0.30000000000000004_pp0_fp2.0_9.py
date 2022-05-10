import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import weakref

from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

# A mixin for RawIOBase tests that defines some utility methods
# and checks for the presence of essential RawIOBase methods.

class BaseTestRawIO(object):

    def setUp(self):
        self.f = self.FileIO(support.TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, 'w+')
        self.assertEqual(self.f.name, support.TESTFN)

    def test_close(self):
        self.assertFalse(self.f.closed)
        self.f.close()
        self.assertTrue(self.f.closed)

    def test_fileno(
