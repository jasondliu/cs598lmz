import io
# Test io.RawIOBase

# Helper to read exactly n bytes, like io.DEFAULT_BUFFER_SIZE
def readall(r, n):
    b = bytearray(n)
    while n:
        m = r.readinto(b)
        if m is None:
            m = 0
        elif m == 0:
            raise EOFError
        n -= m
# Constructor

class BadRawIO(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0

try:
    io.RawIOBase()
except TypeError:
    print('TypeError')
else:
    print('no TypeError')

try:
    BadRawIO()
except TypeError:
    print('TypeError')
else:
    print('no TypeError')

class GoodRawIO(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0

try:
    GoodRawIO()
except TypeError:
    print('
