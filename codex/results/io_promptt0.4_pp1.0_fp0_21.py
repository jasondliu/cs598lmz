import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[:2] = b'xy'
        return 2

buf = bytearray(10)
MyRawIO().readinto(buf)
print(buf)
