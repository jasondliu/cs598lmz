import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b'abc'
    def write(self, b):
        return len(b)

r = MyRawIO()
r.read()
r.write(b'def')
r.seekable()
r.readable()
r.writable()
r.readinto(bytearray(10))
r.seek(0)
r.tell()
r.truncate(10)
r.close()

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self):
        self.raw = MyRawIO()
    def read(self, size=-1):
        return self.raw.read(size)
    def read1(self, size=-1):
        return self.raw.read(size)
    def write(self, b):
        return self.raw.write(b)
    def seek(self, pos, whence=0):
        return self.raw.seek(pos
