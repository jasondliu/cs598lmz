import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.readinto_calls = 0
        self.read_calls = 0
    def readinto(self, buf):
        self.readinto_calls += 1
        assert isinstance(buf, bytearray)
        return super().readinto(buf)
    def read(self, size=-1):
        self.read_calls += 1
        return super().read(size)

# Test that readinto() calls RawIOBase.readinto()
with TestRawIO() as f:
    buf = bytearray(5)
    n = f.readinto(buf)
    assert n is None
    assert f.readinto_calls == 1
    assert f.read_calls == 0

# Test that readinto() calls RawIOBase.read()
class TestRawIO(io.RawIOBase):
    def readinto(self, buf):
        return super().readinto(buf)
    def read(self, size=-1):
