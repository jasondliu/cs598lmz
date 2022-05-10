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
