import io
# Test io.RawIOBase

# Test that io.RawIOBase is a base class for raw binary I/O.

import io
import _pyio as pyio
import unittest

# A test raw stream
class StreamIO(io.RawIOBase):

    def __init__(self, buf=""):
        self._buf = buf

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readall(self):
        return self._buf

    def readinto(self, b):
        b[:] = self._buf
        return len(self._buf)

    def write(self, b):
        self._buf += b
        return len(b)

    def seek(self, pos, whence=0):
        pass

    def tell(self):
        return 0

    def truncate(self, pos=None):
        pass

    def close(self):
        pass

# Test the RawIOBase interface

class RawIOTest(unittest.TestCase):

    def test
