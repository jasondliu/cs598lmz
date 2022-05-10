import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
import errno

from test import support
from test.support import TESTFN, unlink, run_unittest

# Test RawIOBase using a memory buffer

class TestRawIO(io.RawIOBase):

    def __init__(self, initial_bytes=b''):
        self.read_history = []
        self.write_history = []
        self.read_history.append(initial_bytes)
        self.pos = 0

    def readinto(self, b):
        self.read_history.append(b)
        if self.pos >= len(self.read_history[0]):
            return 0
        b[:len(self.read_history[0])-self.pos] = \
            self.read_history[0][self.pos:]
        self.pos = len(self.read_history[0])
        return len(b)

    def write(self, b):
        self.write_history.append(b
