import io
# Test io.RawIOBase
import os
import tempfile
import unittest
import warnings

from test.support import TESTFN, unlink, run_unittest

# XXX(nnorwitz): I've added a deprecation warning to RawIOBase.readall()
# and RawIOBase.read().  These tests should be updated to not use those
# methods.

# For testing tell() and seek() methods
TEST_FILE = tempfile.TemporaryFile()
TEST_FILE.write(b'abcdefghijklmnopqrstuvwxyz')
TEST_FILE.seek(0, 0)

class MockRawIO(io.RawIOBase):

    def __init__(self):
        self.read_history = []
        self.write_history = []
        self.seek_history = []
        self.tell_history = []
        self.readinto_history = []

    def read(self, n=-1):
        self.read_history.append(n)
        return b''

    def write(self, b):
        self.write_history.
