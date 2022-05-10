import io
# Test io.RawIOBase.readinto()

# test readinto() with no argument
class TestRawIOBaseNoArg(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buf = bytearray(b'abcdefghi')

    def readinto(self):
        return super().readinto()

    def read(self, n=-1):
        return self.buf[:n]

# test readinto() with a bytearray argument
class TestRawIOBaseByteArrayArg(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buf = bytearray(b'abcdefghi')

    def readinto(self, b):
        return super().readinto(b)

    def read(self, n=-1):
        return self.buf[:n]

# test readinto() with a memoryview argument
