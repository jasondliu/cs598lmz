import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
import weakref

from test import support

# This is a base class for testing raw I/O.  A derived class should
# override setUp(), which is called at the start of each test method,
# and tearDown(), which is called at the end of each test method.
# The derived class should also set the instance variable 'thetype' to
# the type object that it is testing.

class BaseRawIOBaseTests(unittest.TestCase):

    def setUp(self):
        self.f = self.thetype(self.args)

    def tearDown(self):
        self.f.close()
        self.f = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'mode'), "I/O object has no attribute 'mode'")
        self.assertTrue(hasattr(self.f, 'name'), "I/O object has no attribute 'name'")

    def test_read(self):
        self.assertRa
