import io
# Test io.RawIOBase

import _io

class TestRawIO(_io.RawIOBase):
    # A test RawIO implementation with read(), readinto() and readall().

    def __init__(self, source_bytearray):
        self._source = source_bytearray
        self._read_stack = []
        self._pos = 0
        self._read_stack_pos = 0
        self._max_pos = len(source_bytearray)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def readinto(self, b):
        if self._pos >= self._max_pos:
            return 0
        new_pos = self._pos + len(b)
        to_copy = self._max_pos - self._pos
        if new_pos > self._max_pos:
            to_copy = self._max_pos - self._pos
        else:
            to_copy = len(b)
        b[:to_copy] = self._source[
