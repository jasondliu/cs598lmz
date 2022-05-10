import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must define a read() method.
class BaseTestRawIO(object):
    # Subclasses can override.
    def new_instance(self):
        return self.io.open(TESTFN, 'w+b')

    def setUp(self):
        self.io = support.import_fresh_module('io')
        self.r = self.new_instance()

    def tearDown(self):
        if self.r:
            self.r.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.r.mode, 'w+b')
        self.assertEqual(self.r.name, TESTFN)
        self.assertTrue(self.r.closed)

    def test_read(self):
        self.assertRaises(TypeError, self.r.read
