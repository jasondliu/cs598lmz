import io
# Test io.RawIOBase.readinto

import _io
import io
import sys

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self._buf = buf
        self._offset = 0
    def readinto(self, b):
        o = self._offset
        l = len(b)
        if l > len(self._buf) - o:
            l = len(self._buf) - o
        b[:l] = self._buf[o:o + l]
        self._offset += l
        return l
    def write(self, b):
        o = self._offset
        self._buf[o:o + len(b)] = b
        self._offset += len(b)
        return len(b)

# test readinto
b = bytearray(b'abcdefghij')
r = MyRawIO(b)
b2 = bytearray(5)
n = r.readinto(b2)
assert n == 5
assert b2 == b'abcde'
n = r.readinto
