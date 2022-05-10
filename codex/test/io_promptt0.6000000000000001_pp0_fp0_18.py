import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b = bytearray(b)
        for i in range(len(b)):
            b[i] = i
        return len(b)

try:
    MyRawIO().readinto(bytearray(4))
except Exception as e:
    print(e)

try:
    MyRawIO().readinto(bytearray(1))
except Exception as e:
    print(e)

try:
    MyRawIO().readinto(bytearray(3))
except Exception as e:
    print(e)

# Test io.RawIOBase.readinto1()

class MyRawIO(io.RawIOBase):
    def readinto1(self, b):
        b = bytearray(b)
        for i in range(len(b)):
            b[i] = i
        return len(b)

