import io
# Test io.RawIOBase.readinto() and io.RawIOBase.write() with a memory buffer object.
# This tests both the readinto() and write() methods, since they are symmetric
# and almost the same code.
import io
import sys
import builtins

class TestRawIOBase(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        self._seek_count += 1

    def close(self):
        self._closed = True

    def __init__(self, magic_string):
        self._seek_count = 0
        self._closed = False
        self._buf = bytearray(magic_string.encode())

class TestRawIOBaseSize0(TestRawIOBase):

    def __init__(self, magic_string):
        super().__init__(magic_string)
        self._buf.clear()

