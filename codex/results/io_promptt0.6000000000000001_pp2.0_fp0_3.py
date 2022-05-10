import io
# Test io.RawIOBase.readall

class TestRawIO(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        b[:] = b'\x00\x01\x02\x03\x04\x05\x06\x07'
        return 8

r = TestRawIO()
print(r.readall())
r.close()
print(r.readall())
