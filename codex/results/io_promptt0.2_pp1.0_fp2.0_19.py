import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"abc"
        return 3

rawio = MyRawIO()
b = bytearray(5)
n = rawio.readinto(b)
print(n, b)

# Test io.RawIOBase.readinto1()

class MyRawIO(io.RawIOBase):
    def readinto1(self, b):
        b[:3] = b"abc"
        return 3

rawio = MyRawIO()
b = bytearray(5)
n = rawio.readinto1(b)
print(n, b)
