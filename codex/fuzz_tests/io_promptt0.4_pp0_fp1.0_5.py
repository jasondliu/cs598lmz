import io
# Test io.RawIOBase.readinto()

import io
import os
import struct
import sys
import tempfile
import unittest
from test import test_support as support
from test.test_support import TESTFN

# Test RawIOBase.readinto()

class TestRawIO(io.RawIOBase):

    def __init__(self, test_string):
        self.string_len = len(test_string)
        self.read_len = 0
        self.read_stack = []

    def readinto(self, b):
        if self.read_len == self.string_len:
            return 0
        length = min(len(b), self.string_len - self.read_len)
        self.read_stack.append((self.read_len, length))
        self.read_len += length
        b[:length] = bytearray(b"x" * length)
        return length

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.read_len
