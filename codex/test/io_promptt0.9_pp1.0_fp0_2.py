import io
# Test io.RawIOBase.readinto

class TestRawIO(io.RawIOBase):
    def __init__(self):
        pass

    def readinto(self, b):
        b[:6] = b"foobar"
        return 6

buf = bytearray(10)
TestRawIO().readinto(buf)

buf
