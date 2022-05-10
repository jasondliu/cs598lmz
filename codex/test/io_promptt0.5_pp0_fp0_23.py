import io
# Test io.RawIOBase

# Test that RawIOBase.readinto() is implemented.

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b'a'*len(b)
        return len(b)
    def readable(self):
        return True

MyRawIO().readinto(bytearray(10))

# Test that RawIOBase.readinto() is not implemented.

class MyRawIO(io.RawIOBase):
    def readable(self):
        return True

