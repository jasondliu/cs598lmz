import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

class TestRawIO(io.RawIOBase):

    def __init__(self, test_string):
        self._read_stack = []
        self._write_stack = []
        self._reads = 0
        self._writes = 0
        self._seek_count = 0
        self._closed = False
        self._test_string = test_string

    def readinto(self, b):
        self._reads += 1
        if self._read_stack:
            data = self._read_stack.pop(0)
        else:
            data = self._test_string
        b[:len(data)] = data
        return len(data)

    def write(self, b):
        self._writes += 1
        self._write_stack.append(b)
        return len(b)

    def seekable(self):
        return True

    def seek(self, pos, whence=0
