import io
# Test io.RawIOBase
import io

class RawI(io.RawIOBase):

    def read(self, n=-1):
        return b'abc'

    def write(self, b):
        return len(b)

r = RawI()
print(r.read())
print(r.read(2))
print(r.read(4))
print(r.read())
