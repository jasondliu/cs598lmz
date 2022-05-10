import io
# Test io.RawIOBase
try:
    f = io.BytesIO(b"abc")
    f.readinto1(bytearray(1))
except AttributeError:
    print('SKIP')
    raise SystemExit

class TestIO(io.RawIOBase):
    def readinto1(self, b):
        return super().readinto1(b)

class TestIO2(io.RawIOBase):
    def readinto1(self, b):
        return super().readinto1(b)
    def readable(self):
        return False

class TestIO3(io.RawIOBase):
    def readinto1(self, b):
        return super().readinto1(b)
    def readinto(self, b):
        return super().readinto(b)

try:
    TestIO()
except TypeError:
    print('SKIP')
    raise SystemExit

# TestRawIOBase
