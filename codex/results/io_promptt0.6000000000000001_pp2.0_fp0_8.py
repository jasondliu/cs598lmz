import io
# Test io.RawIOBase

import warnings
import unittest
from test import support

class MockRawIO(io.RawIOBase):

    def __init__(self):
        self.readinto_calls = 0
        self.read_calls = 0
        self.write_calls = 0
        self.seek_calls = 0
        self.tell_calls = 0
        self.closed = 0

    def readinto(self, b):
        self.readinto_calls += 1
        raise OSError

    def read(self, n=-1):
        self.read_calls += 1
        raise OSError

    def write(self, b):
        self.write_calls += 1
        raise OSError

    def seek(self, pos, whence=0):
        self.seek_calls += 1
        raise OSError

    def tell(self):
        self.tell_calls += 1
        raise OSError

    def close(self):
        self.closed = 1

class RawIOTest(unittest
