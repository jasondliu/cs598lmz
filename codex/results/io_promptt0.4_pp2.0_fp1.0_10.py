import io
# Test io.RawIOBase
import io
import sys

class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b"a" * n

rawio = RawI()
print(rawio.read())
print(rawio.read(10))
print(rawio.read1(10))
print(rawio.readinto(bytearray(10)))
print(rawio.readinto1(bytearray(10)))
print(rawio.readinto(memoryview(bytearray(10))))
print(rawio.readinto1(memoryview(bytearray(10))))
print(rawio.readall())
print(rawio.read1())
print(rawio.readinto1(bytearray(10)))
print(rawio.read1(10))
print(rawio.readinto1(bytearray(10)))
print(rawio.read())
print(rawio.read1())
print(rawio.readinto1(bytearray(10)))
print(rawio.read())
print(
