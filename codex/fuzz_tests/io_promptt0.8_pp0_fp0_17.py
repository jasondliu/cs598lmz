import io
# Test io.RawIOBase.


class MyRawIOBase(io.RawIOBase):
    def __init__(self, dummy):
        self.readable = self.writable = False

    def readinto(self, b):
        b[17:23] = b"xyzzy"
        return len(b)

MyRawIO = MyRawIOBase

a = bytearray(100)
r = MyRawIO(None)
r.readable = True
r.readinto(a)
print(a[17:23])
r.writable = True
r.write(b"abcde")
