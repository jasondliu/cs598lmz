import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# Base class for testing RawIOBase
class BaseTestRawIO(object):
    # Subclass must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.b_prefix
    # - self.u_prefix
    # - self.b_suffix
    # - self.u_suffix
    # - self.b_mode
    # - self.u_mode

    def setUp(self):
        self.f = self.io.open(self.filename, self.mode)

    def tearDown(self):
        if not self.f.closed:
            self.f.close()
        support.unlink(self.filename)

    def test_attributes(self):
        self.assertEqual(self.f.mode, self.mode)
        self.assertEqual(self.f.name, self.filename)
        self.assertEqual(self.f.closed, False)

    def test_read(self
