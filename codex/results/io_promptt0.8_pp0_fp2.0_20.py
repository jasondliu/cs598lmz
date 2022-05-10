import io
# Test io.RawIOBase

import io
import unittest

from test import support

# A test raw file system that can be passed to RawIOBase constructors.
TESTFN = support.TESTFN
# This module is implemented on top of the _pyio module which was
# introduced after Python 3.2, hence it's not available on 3.2.
@unittest.skipIf(io.RawIOBase.__module__ == 'io',
    'test needs features introduced in Python 3.3')
class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def read(self, n=-1):
        """Read n bytes from the file"""
        return self.f.read(n)

    def write(self, b):
        """Write the bytes or bytearray b to the file"""
        self.f.seek(0, 2)
        if isinstance(b, memoryview):
            b = b.tobytes()
        self.f.write(b)

    def tell
