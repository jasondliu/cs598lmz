import io
# Test io.RawIOBase
class MyIO(io.RawIOBase):
    def read(self, size = -1):
        return b'1' * size

    def readall(self):
        return b'2' * 1024

    def readinto(self, b):
        b[:] = b'4' * len(b)

    def write(self, b):
        return len(b)

fp = MyIO()
print(fp.read())
print(fp.readall())
b = bytearray(64)
fp.readinto(b)
print(b)
print(fp.write(b'5'))

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self):
        self.fileobj = io.BytesIO(b'123456')

    def read(self, size = -1):
        return self.fileobj.read(size)

    def read1(self, size = -1):
        return self.fileobj.read(size)

    def write(self, data):
