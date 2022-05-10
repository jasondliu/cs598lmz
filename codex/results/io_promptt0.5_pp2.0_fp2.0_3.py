import io
# Test io.RawIOBase
#
# Copyright (C) 2005, 2006 Python Software Foundation
# Author: Ben Gertzfield
# Contact: email-sig@python.org

"""Test io.RawIOBase"""

import io
import unittest

from test.support import run_unittest

class TestRawIOBase(unittest.TestCase):

    def test_attributes(self):
        # Make sure we have the attributes we want.
        self.assertTrue(hasattr(io.RawIOBase, 'read'),
                        'RawIOBase is missing a read() method')
        self.assertTrue(hasattr(io.RawIOBase, 'readinto'),
                        'RawIOBase is missing a readinto() method')
        self.assertTrue(hasattr(io.RawIOBase, 'write'),
                        'RawIOBase is missing a write() method')

    def test_read(self):
        # Test RawIOBase.read()

        # Test a read() implementation that returns an empty string
        class TestRawIO(io.RawIOBase):
            def read(self, n=-
