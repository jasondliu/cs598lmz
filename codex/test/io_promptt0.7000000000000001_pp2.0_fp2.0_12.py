import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def readall(self):
        return b"abc"

print(MyRawIO().readall())

# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[0:3] = b"abc"
        return 3

b = bytearray(10)
print(MyRawIO().readinto(b), b[0:3], b[3:10])

# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        return 0

b = bytearray(10)
print(MyRawIO().readinto(b), b[0:10])

# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        raise OSError

b = bytearray(10)

