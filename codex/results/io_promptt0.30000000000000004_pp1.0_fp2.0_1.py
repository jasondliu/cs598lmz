import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00"*n

rawio = MyRawIO()
assert rawio.read(10) == b"\x00"*10
assert rawio.read(0) == b""
assert rawio.read() == b""
# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def read(self, n=-1):
        return self.raw.read(n)

bufferedio = MyBufferedIO(rawio)
assert bufferedio.read(10) == b"\x00"*10
assert bufferedio.read(0) == b""
assert bufferedio.read() == b""
# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, n=-1):
        return "x"*n

textio = MyTextIO()
assert textio
