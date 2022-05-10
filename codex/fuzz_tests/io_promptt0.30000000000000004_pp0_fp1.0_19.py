import io
# Test io.RawIOBase

import _io
from test.support import run_unittest, import_module

# Test RawIOBase using a memory buffer

class TestRawIO(io.RawIOBase):

    def __init__(self, initial_bytes=b''):
        self.read_history = []
        self.write_history = []
        self.read_history.append(initial_bytes)

    def readinto(self, b):
        data = self.read_history[0]
        del self.read_history[0]
        n = len(b)
        b[:len(data)] = data
        return len(data)

    def write(self, b):
        self.write_history.append(b)
        return len(b)

    def read(self, n=-1):
        data = self.read_history[0]
        del self.read_history[0]
        if n >= 0:
            data = data[:n]
        return data

    def seekable(self):
        return True

    def seek(self, pos, whence
