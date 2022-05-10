import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing the RawIOBase interface.
# Subclasses must override read(), seek(), and write().
class BaseRawIO(io.RawIOBase):

    def read(self, n=-1):
        raise NotImplementedError

    def seek(self, n, whence=0):
        raise NotImplementedError

    def write(self, b):
        raise NotImplementedError

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        data = self.read(len(b))
        if not data:
            return 0
        b[:len(data)] = data
        return len(data)

    def readall(self):
        chunks = []
        while True:
            data = self.read(1024)
            if not data:
                break
            chunks
