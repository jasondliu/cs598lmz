import io
# Test io.RawIOBase.readinto

import _io

class TestRawIO(io.RawIOBase):

    def readable(self):
        return True

    def readinto(self, b):
        b[0] = ord('h')
        b[1] = ord('i')
        return 2


r = TestRawIO()
b = bytearray(5)
n = r.readinto(b)
assert n == 2
assert b == b'hi\x00\x00'
n = r.readinto(b)
assert n == 2
assert b == b'hi\x00\x00'

# Test io.BufferedIOBase.readinto

class TestBufferedIO(io.BufferedIOBase):

    def readable(self):
        return True

    def readinto(self, b):
        b[0] = ord('h')
        b[1] = ord('i')
        return 2


r = TestBufferedIO()
b = bytearray(5)
n = r.readinto(b)
assert n == 2
assert
