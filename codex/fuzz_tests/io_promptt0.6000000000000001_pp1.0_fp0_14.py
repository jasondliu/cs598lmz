import io
# Test io.RawIOBase.readinto()

class ReadintoTest:
    def __init__(self, data):
        self.data = data

    def readinto(self, b):
        b[:len(self.data)] = self.data
        return len(self.data)

r = ReadintoTest(b"abc")

b = bytearray(5)
n = r.readinto(b)
print(n, b)

b = bytearray(2)
n = r.readinto(b)
print(n, b)

b = bytearray(1)
n = r.readinto(b)
print(n, b)

b = bytearray(4)
n = r.readinto(b)
print(n, b)

# Test io.RawIOBase.readinto1()

class Readinto1Test:
    def __init__(self, data):
        self.data = data

    def readinto1(self, b):
        b[:1] = self.data[:1]
       
