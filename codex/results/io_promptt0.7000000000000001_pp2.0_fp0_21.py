import io
# Test io.RawIOBase, derived from io.IOBase

import unittest
from test import support

# The io module uses a custom metaclass which raises an ImportError
# when the _io module is not built.
try:
    import _io
except ImportError:
    raise unittest.SkipTest("_io module not built")

# A simple RawIOBase-alike which doesn't do anything.

class MockRawIO(io.RawIOBase):
    def read(self, n=-1):
        pass
    def readall(self):
        pass
    def readinto(self, b):
        pass
    def write(self, b):
        pass

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        rawio = MockRawIO()
        self.assertRaises(TypeError, rawio.read)
        self.assertRaises(TypeError, rawio.read, 'x')
        self.assertRaises(TypeError, rawio.read, b'')
        self
