import io
# Test io.RawIOBase

import unittest
import os

from test import test_support

class MockRawIO(io.RawIOBase):

    def __init__(self, read_stack=None, readall_stack=None,
                 write_stack=None, seek_stack=None,
                 tell_stack=None, truncate_stack=None,
                 fileno_stack=None):
        self.read_stack = read_stack or []
        self.readall_stack = readall_stack or []
        self.write_stack = write_stack or []
        self.seek_stack = seek_stack or []
        self.tell_stack = tell_stack or []
        self.truncate_stack = truncate_stack or []
        self.fileno_stack = fileno_stack or []

    def read(self, size=-1):
        return self.read_stack.pop(0)

    def readall(self):
        return self.readall_stack.pop(0)

    def write(self, b):
        self.write_stack.append(b)
