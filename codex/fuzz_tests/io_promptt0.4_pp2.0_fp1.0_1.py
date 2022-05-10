import io
# Test io.RawIOBase

import unittest
import weakref
from test import test_support

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"xyzzy"*n
    def write(self, b):
        pass
    def seekable(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return True

class MyRawIO1(MyRawIO):
    def readable(self):
        return False

class MyRawIO2(MyRawIO):
    def writable(self):
        return False

class MyRawIO3(MyRawIO):
    def readable(self):
        return False
    def writable(self):
        return False

class MyRawIO4(MyRawIO):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True

class MyRawIO5(MyRawIO):
    def readable(self):
        return True
    def writable
