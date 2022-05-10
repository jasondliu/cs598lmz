import io
# Test io.RawIOBase
import sys
import os
import types
import operator
import _io
import tempfile
import unittest
import warnings

import test.support
from test.support import TestFailed, run_unittest

def check(ok):
    if not ok:
        raise TestFailed('an error occurred in the underlying buffer object')

class MyIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        check(len(b) >= 3)
        b[0] = ord('s')
        b[1] = ord('p')
        b[2] = ord('a')
        return 3

    def write(self, b):
        check(b == b'xyz')
        return 3

    def seek(self, pos, whence=0):
        if whence == 1:
            check(pos == -3)
        elif whence == 2:
            check(pos == 3)
        else
