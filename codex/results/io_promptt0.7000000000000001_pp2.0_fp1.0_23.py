import io
# Test io.RawIOBase

import os
import unittest
from test import test_support


class RawIOBaseTest(unittest.TestCase):

    @unittest.skipUnless(hasattr(os, 'fsencode'),
                         "test needs os.fsencode()")
    def test_attributes(self):
        # Make sure all expected attributes are present.
        if hasattr(os, 'lseek'):
            self.assertTrue(hasattr(io.RawIOBase, "seek"))
            self.assertTrue(hasattr(io.RawIOBase, "tell"))
        self.assertTrue(hasattr(io.RawIOBase, "read"))
        self.assertTrue(hasattr(io.RawIOBase, "readinto"))
        self.assertTrue(hasattr(io.RawIOBase, "write"))

    def test_read(self):
        # Make sure reading 0 bytes returns b'' and doesn't raise EOFError
        self.assertEqual(io.BytesIO().read(0), b"")

    def test_readinto(self):
        # Make sure
