import io
# Test io.RawIOBase.readall()

# Test for issue #11657: reading from a RawIOBase object should not
# mutate its position attribute.

class TestRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00" * n

def test_readall():
    r = TestRawIO()
    assert r.readall() == b"\x00" * (5 * io.DEFAULT_BUFFER_SIZE)
    assert r.readall() == b"\x00" * (5 * io.DEFAULT_BUFFER_SIZE)
    assert r.readall() == b"\x00" * (5 * io.DEFAULT_BUFFER_SIZE)

# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b"\x00" * len(b)
        return len(b)

def test_readinto():
    r = TestRawIO()
