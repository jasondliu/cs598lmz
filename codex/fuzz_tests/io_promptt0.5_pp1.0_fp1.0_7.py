import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        b[:] = b'\x00'*n
        return n

    def write(self, b):
        return len(b)

r = MyRawIO()

buf = bytearray(100)
n = r.readinto(buf)
print(n)

n = r.write(b'abc')
print(n)

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def _flush(self):
        pass

    def _close(self):
        pass

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return self.raw.readinto(b)

    def write(self, b):
        return self.raw.write(b
