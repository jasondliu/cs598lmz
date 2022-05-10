import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
from test import support

class TestRawIO(io.RawIOBase):

    def __init__(self, test_string):
        self.string_len = len(test_string)
        self.read_len = 0
        self.read_stack = []

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.read_len = offset
        elif whence == 1:
            self.read_len += offset
        elif whence == 2:
            self.read_len = self.string_len + offset
        if self.read_len < 0:
            self.read_len = 0
        if self.read_len > self.string_len:
            self.read_len = self.string_len

    def tell(self):
        return self.read_len

    def readinto(self, b):
        data = self.read(
