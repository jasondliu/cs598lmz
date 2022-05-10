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
