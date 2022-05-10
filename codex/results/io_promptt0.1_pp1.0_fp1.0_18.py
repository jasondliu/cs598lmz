import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # Subclasses must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.bmode
    # - self.create_file()

    def setUp(self):
        self.create_file()
        self.f = io.open(self.filename, self.mode)

    def tearDown(self):
        if self.f:
            self.f.close()
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def test_attributes(self):
        self.assertEqual(self.f.mode, self.bmode)
        self.assertEqual(self.f.name, self.filename)
        self.assertEqual(self.f.closed, False)

    def test_close(self):
        self.f.close()

