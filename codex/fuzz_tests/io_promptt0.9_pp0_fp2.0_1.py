import io
# Test io.RawIOBase
from io import RawIOBase, BlockingIOError, UnsupportedOperation, SEEK_SET
from array import array
import types

from test import test_support
import platform
from test.support import run_unittest, precisionbigmemtest
import weakref

# Set to True to print each block read and written, along with a count.
DEBUG = False

class MyIO(RawIOBase):

    def __init__(self):
        RawIOBase.__init__(self)
        self.pos = 0
        self.read_stack = []
        self.write_stack = []
        self._write_stack = []
        self._read_stack = []
        self._extraneous_reads = 0

    def readinto(self, b):
        DEBUG and print("readinto", len(b))
        if not self.read_stack:
            raise BlockingIOError
        cur_len, res = self.read_stack[0]
        del self.read_stack[0]
        off = 0
        r = memoryview(res)[off:off+cur_
