import io
# Test io.RawIOBase
import io, random

class RawRandom(io.RawIOBase):
    def readinto(self, b):
        for i in range(len(b)):
            b[i] = random.randint(0, 255)
        return len(b)

r = RawRandom()
print(r.read(10))

# Test io.BufferedIOBase
import io, random

class BufferedRandom(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def _fill(self, n):
        b = bytearray(n)
        n = self.raw.readinto(b)
        self._set_read_ptr(0)
        self._set_read_end(n)
        self._set_read_buf(b)
    def read(self, n=-1):
        if n >= 0 and n <= self.raw.readinto.__defaults__[0]:
            return super().read(n)
        else:
            return self.raw.read(n)
   
