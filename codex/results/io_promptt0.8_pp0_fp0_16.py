import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=0):
        return b''
    def write(self, buf):
        return 0
m = MyRawIO()
assert m.readable()
assert m.writable()
assert not m.seekable()

try:
    b = m.readinto(memoryview(bytearray(10)))
except TypeError:
    pass

class MyRawIO(io.RawIOBase):
    def read(self, n=0):
        return b''
    def write(self, buf):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return False
m = MyRawIO()
assert m.readable()
assert m.writable()
assert not m.seekable()


class MyRawIO(io.RawIOBase):
    def read(self, n=0):
        return b''
    def write(self, buf):
        return 0

m = MyRawIO()
