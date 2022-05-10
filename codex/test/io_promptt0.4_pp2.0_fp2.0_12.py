import io
# Test io.RawIOBase
import io
import sys

class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n

class RawO(io.RawIOBase):
    def write(self, b):
        self.b = b

class RawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x'*n
    def write(self, b):
        self.b = b

