import io
# Test io.RawIOBase

import io
import sys
import unittest

# This is a base class for testing IO.  It should not be used directly.
class BaseTestRawIO(io.RawIOBase):
    # The concrete subclass should override the read, readinto and write
    # methods.

    def __init__(self, testcase, bufsize=-1):
        self.testcase = testcase
        self.bufsize = bufsize
        self.read_stack = []
        self.write_stack = []

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.read(len(b))
        if len(data) > 0:
            b[:len(data)] = data
        return len(data)

    def seek(self, pos, whence=0):
        return self.seek_impl(pos, whence)

    def tell(self):
        return self.seek(0, 1)

