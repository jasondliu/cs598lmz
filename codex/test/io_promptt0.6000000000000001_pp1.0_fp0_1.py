import io
# Test io.RawIOBase.readall()

class TestRawIO(io.RawIOBase):

    def readall(self):
        return b"foobar"

try:
    f = TestRawIO()
    f.readall()
except Exception as err:
    print(err)

# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):

    def readinto(self, b):
        b[2:6] = b"bar"
        return 4

try:
    f = TestRawIO()
    b = bytearray(6)
    f.readinto(b)
    print(b)
except Exception as err:
    print(err)
