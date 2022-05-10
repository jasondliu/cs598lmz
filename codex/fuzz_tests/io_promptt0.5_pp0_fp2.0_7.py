import io
# Test io.RawIOBase.readinto()
#
# This test checks that the readinto() method of RawIOBase works
# properly.
#
# readinto() is supposed to read data into a pre-allocated buffer.
#
# It was first introduced in Python 3.1.
#
# This test checks that the method works even when the underlying
# buffer is not writable.  In Python 3.1, the method was only
# implemented for writable buffers.
#
# See http://bugs.python.org/issue11395

import array
import io
import unittest

class TestRawIO(io.RawIOBase):
    def __init__(self, data):
        self._data = data
        self._pos = 0

    def readinto(self, b):
        n = min(len(self._data) - self._pos, len(b))
        if n > 0:
            b[:n] = self._data[self._pos:self._pos+n]
            self._pos += n
            return n
        return 0

    def readable(self):
        return True


