import io
# Test io.RawIOBase

import io

class TestRawIO(io.RawIOBase):

    def read(self, n=-1):
        return b"x" * n

    def write(self, b):
        return len(b)

def test_read():
    r = TestRawIO()
    assert r.read(0) == b""
    assert r.read(1) == b"x"
    assert r.read(2) == b"xx"
    assert r.read() == b""
    assert r.read() == b""
    assert r.read1(1) == b"x"
    assert r.readinto(bytearray(b"xxx")) == 3
    assert r.readinto1(bytearray(b"xxx")) == 3
    assert r.readinto(bytearray(b"xxx")) == 0
    assert r.readinto1(bytearray(b"xxx")) == 0
    assert r.readinto(bytearray(b"xxx")) == 0
