import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        for i in range(n):
            b[i] = ord('A') + i
        return n

rawio = MyRawIO()
b = bytearray(10)
n = rawio.readinto(b)
len(b) == 10
n == 10
b == bytearray(b'ABCDEFGHIJ')

# Test io.BufferedIOBase

class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.__raw = raw
    def read(self, n = -1):
        b = bytearray(n)
        n = self.raw.readinto(b)
        return memoryview(b)[:n]

@property
def raw(self):
    return self.__raw

bufferedio = MyBufferedIO(rawio)
b = bufferedio.read(10)
len(b) == 10
b
