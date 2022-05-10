import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):

    def readinto(self, b):
        b[0:3] = b'foo'
        return 3

    def readable(self):
        return True


