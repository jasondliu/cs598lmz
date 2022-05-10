import io
# Test io.RawIOBase
import io
import _io

class MyRawIO(io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def readinto(self, b):
        b[:] = b'foo'
        return 3

    def readall(self):
        return b'foo'

r = MyRawIO()
assert r.readable() is True
assert r.writable() is False
assert r.seekable() is True
assert r.readall() == b'foo'
assert r.read(2) == b'fo'
assert r.read() == b'o'
assert r.readinto(bytearray(3)) == 3
assert r.readinto(bytearray(3)) == 0
assert r.readinto(bytearray(2)) == 0
# Test io.RawIOBase.readinto() writes past the end of the buffer
import io
import _io

class MyRawIO(io.RawIOBase):
    def readable
