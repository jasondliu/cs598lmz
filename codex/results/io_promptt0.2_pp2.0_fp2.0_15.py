import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _io

# Base class for testing.  Doesn't define read or readline.
class BaseTestRawIO(io.RawIOBase):

    def __init__(self, testcase):
        self._testcase = testcase
        self.mode = None
        self.closed = False
        self.softspace = False
        self.pos = 0
        self.read_stack = []
        self.write_stack = []
        self.seek_stack = []
        self.tell_stack = []
        self.fileno_stack = []
        self.flush_stack = []
        self.close_stack = []
        self.isatty_stack = []

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[
