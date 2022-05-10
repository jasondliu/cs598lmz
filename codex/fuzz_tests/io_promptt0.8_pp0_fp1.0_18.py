import io
# Test io.RawIOBase

import unittest
import io

from test import support
from test.support import HASH_ALGORITHMS

TESTFN = support.TESTFN

class BaseTest:
    # Helper base class with a testable close() method.

    def close(self):
        """Simply record that the method has been called."""
        self.closed = True

    def get_closed(self):
        return self.closed

    def set_closed(self, value):
        self.closed = value

    def assert_closed_state(self, closed):
        self.assertEqual(self.get_closed(), closed)

    def tearDown(self):
        del self.closed

class AutoFileTests(BaseTest, unittest.TestCase):
    # Test the functionality of the 'with' statement.

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w')
        self.set_closed(False)

    def test_closed_attr(self):
        self.assertEqual(self.f.closed
