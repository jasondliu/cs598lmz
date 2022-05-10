import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        # RawIOBase defines a number of attributes that must be present
        # on any implementation.  This tests that the attributes exist
        # and have the correct types.
        rawio = io.RawIOBase()
        self.assertIsInstance(rawio.mode, str)
        self.assertIsInstance(rawio.name, (str, type(None)))
        self.assertIsInstance(rawio.closed, bool)
        self.assertIsInstance(rawio.isatty(), bool)
        self.assertIsInstance(rawio.readable(), bool)
        self.assertIsInstance(rawio.writable(), bool)
        self.assertIsInstance(rawio.seekable(), bool)
        self.assertIsInstance(rawio.fileno(), (int, type(None)))
        self.assertIsInstance(rawio.flush(), None)
        self.assertIsInstance(rawio.close(), None)
        self.assert
