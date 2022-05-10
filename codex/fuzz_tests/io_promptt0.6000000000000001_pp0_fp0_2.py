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
assert buf == b"st"
assert r.readinto(buf) == 2
assert buf == b"te"

buf = bytearray(1)
assert r.readinto(buf) == 1
assert buf == b"t"
assert r.readinto(buf) == 1
assert buf == b"e"

buf = bytearray(3)
assert r.readinto(buf) == 3
assert buf == b"tes"

buf = bytearray(4)
assert r.readinto(buf) == 4
assert
