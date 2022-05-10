import io
# Test io.RawIOBase

import _testbuffer
from test import support, test_io
import unittest
import weakref
import os


class RawIOTest(unittest.TestCase):

    class testrawio(io.RawIOBase):
        def __init__(self, filename):
            f = open(filename, "rb")
            self.read_buf = f.read()
            f.close()
            self.read_pos = 0

        def readinto(self, buf):
            max_bytes = len(buf)
            if max_bytes > len(self.read_buf) - self.read_pos:
                max_bytes = len(self.read_buf) - self.read_pos
            buf[0:max_bytes] = self.read_buf[self.read_pos:self.read_pos+max_bytes]
            self.read_pos += max_bytes
            return max_bytes

    def test_close_is_idempotent(self):
        f = self.testrawio(test_io.__file__)
        f.close
