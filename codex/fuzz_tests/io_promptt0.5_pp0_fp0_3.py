import io
# Test io.RawIOBase

import unittest
from test import support

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"xyzzy"

    def write(self, b):
        return len(b)

class MyRawIO2(io.RawIOBase):
    def read(self, n=-1):
        return b"xyzzy"

    def write(self, b):
        return len(b)

    def seekable(self):
        return True

    def tell(self):
        return 42

    def seek(self, pos, whence=0):
        pass

class MyRawIO3(io.RawIOBase):
    def read(self, n=-1):
        return b"xyzzy"

    def write(self, b):
        return len(b)

    def seekable(self):
        return True

    def tell(self):
        return 42

    def seek(self, pos, whence=0):
        pass

    def readable(self):
        return True

    def writable(self):

