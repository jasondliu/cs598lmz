import io
# Test io.RawIOBase - a file-like object with read and write support

import _io
import unittest
from test.support import test_main
import weakref
try:
    import threading
except ImportError:
    threading = None

# io.RawIOBase is not a public type.  Use the C implementation directly.
RawIOBase = _io._IOBase

class MyBytesRawIO(RawIOBase):
    def __init__(self, buf):
        RawIOBase.__init__(self)
        self.read_history = []
        self.write_history = []
        self.read_stack = [buf]
        self.buf = buf

    def readall(self):
        if self.read_stack:
            data = self.read_stack[0]
            self.read_stack = []
            self.read_history.append('readall')
            return data
        else:
            self.read_history.append('readall-eof')
            return b""

    def readinto(self, buf):
        data = self.read(len(
