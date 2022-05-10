import io
# Test io.RawIOBase

# io.RawIOBase is not implemented through an _io.IOBase subclass,
# and has its own set of tests

import io
import io as io_mod
import os
import operator
import pickle
import random
import string
import traceback
import unittest
from test import support


class MockRawIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def fileno(self):
        return 42

    def isatty(self):
        return False

    def readinto(self, buf):
        return 0

    def read(self, n=-1):
        return b''

    def write(self, b):
        pass

    def seek(self, offset, whence=0):
        pass

    def tell(self):
        return 0

    def truncate(self, pos=None):
        pass

    def flush(self):
        pass


class InheritingRawIO(MockRawIO):
    """This class
