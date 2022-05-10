import io
# Test io.RawIOBase.readinto()

import _io

class TestRawIO(io.RawIOBase):

    def readinto(self, b):
        b[0:5] = b'abcde'
        return 5

buf = bytearray(5)
TestRawIO().readinto(buf)
print(buf)
