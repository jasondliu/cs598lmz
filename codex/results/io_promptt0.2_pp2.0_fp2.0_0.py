import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[0:3] = b"abc"
        return 3

buf = bytearray(5)
MyRawIO().readinto(buf)
print(buf)

buf = bytearray(5)
MyRawIO().readinto(memoryview(buf))
print(buf)

buf = bytearray(5)
MyRawIO().readinto(memoryview(buf)[1:])
print(buf)

buf = bytearray(5)
MyRawIO().readinto(memoryview(buf)[1:4])
print(buf)

buf = bytearray(5)
MyRawIO().readinto(memoryview(buf)[1:4:2])
print(buf)

buf = bytearray(5)
MyRawIO().readinto(memoryview(buf)[1:4:2].cast('B'))
print(buf)

buf = bytearray(5)
