import io
# Test io.RawIOBase.readinto()

import support

BUFSIZE = 1000

class MyReadInto(io.RawIOBase):
    def readinto(self, b):
        return 0

class MyRead(io.RawIOBase):
    def read(self, n=-1):
        return b''

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b'a'*min(len(b), BUFSIZE)
        return len(b)
    def read(self, n=-1):
        return b'a'*min(n, BUFSIZE)

class MyReadIntoNonNone(io.RawIOBase):
    def readinto(self, b):
        b[:] = b'a'*min(len(b), BUFSIZE)
        return len(b)

r = MyReadInto()
try:
    r.readinto(bytearray(BUFSIZE))
except TypeError:
    pass
else:
    raise support.TestError("readinto() didn't
