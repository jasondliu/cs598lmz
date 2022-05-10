import io
# Test io.RawIOBase

import unittest
import weakref
from test import support
from test.support import TESTFN, run_unittest

class MyRawIO(io.RawIOBase):

    def __init__(self):
        self.read_stack = []
        self.write_stack = []
        self.reads = []
        self.writes = []

    def readinto(self, b):
        self.reads.append(b)
        self.read_stack, stack = stack, self.read_stack
        while stack:
            b[:len(stack[0])] = stack[0]
            del stack[0]
            b = b[len(stack[0]):]
            if not b:
                break
        self.read_stack = stack
        return len(b)

    def write(self, b):
        self.writes.append(b)
        self.write_stack.append(b)
        return len(b)

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
       
