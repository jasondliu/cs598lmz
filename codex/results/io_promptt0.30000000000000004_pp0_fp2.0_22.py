import io
# Test io.RawIOBase

import io
import unittest

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "RawIOBase is missing the 'mode' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "RawIOBase is missing the 'name' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'close'),
                        "RawIOBase is missing the 'close' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'closed'),
                        "RawIOBase is missing the 'closed' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'fileno'),
                        "RawIOBase is missing the 'fileno' attribute")
        self.assertTrue(hasattr(io.RawIOBase, 'isatty'),
                        "RawIOBase is missing the 'isatty' attribute")
        self.assertTrue(hasattr(io.RawIOBase, '
