import io
# Test io.RawIOBase

# Check that readinto() returns None
class TestRawIOBase(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return None

buf = bytearray(5)
f = TestRawIOBase()
assert f.readinto(buf) is None
assert buf == b'\0\0\0\0\0'

# Check that readinto() returns 0
class TestRawIOBase(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 0

buf = bytearray(5)
f = TestRawIOBase()
assert f.readinto(buf) == 0
assert buf == b'\0\0\0\0\0'

# Check that readinto() returns a positive integer
class TestRawIOBase(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        return 2

buf = bytearray(5)
f = Test
