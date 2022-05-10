import io
# Test io.RawIOBase.readinto()

testbuf = bytearray(b"test")

class TestRawIO(io.RawIOBase):
    def readinto(self, buf):
        if len(buf) > 4:
            raise ValueError
        buf[:] = testbuf[:len(buf)]
        return len(buf)

r = TestRawIO()
buf = bytearray(2)
assert r.readinto(buf) == 2
assert buf == b"te"
assert r.readinto(buf) == 2
