import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class MockRawIO(io.RawIOBase):
    def __init__(self, read_stack=None, readall_stack=None,
                 write_stack=None, seek_stack=None,
                 readable_val=True, writable_val=True,
                 seekable_val=True, readinto_val=None):
        self.read_stack = read_stack or []
        self.readall_stack = readall_stack or []
        self.write_stack = write_stack or []
        self.seek_stack = seek_stack or []
        self.readable_val = readable_val
        self.writable_val = writable_val
        self.seekable_val = seekable_val
        self.readinto_val = readinto_val

    def read(self, n=-1):
        return self.read_stack.pop(0)

    def readall(self):
        return self.readall_stack.pop(0)

    def write(
