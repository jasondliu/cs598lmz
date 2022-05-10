import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support


class MyRawIO(_io.RawIOBase):

    def __init__(self):
        self.read_stack = []
        self.write_stack = []
        self.seek_stack = []
        self.tell_stack = []
        self.flush_stack = []
        self.close_stack = []

    def read(self, n=-1):
        self.read_stack.append(n)
        return b''

    def write(self, b):
        self.write_stack.append(b)

    def seek(self, pos, whence=0):
        self.seek_stack.append((pos, whence))

    def tell(self):
        self.tell_stack.append(None)
        return 0

    def flush(self):
        self.flush_stack.append(None)

    def close(self):
        self.close_stack.append(None)


class TestRawIOBase(unittest.TestCase):

    def test
