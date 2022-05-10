import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"x" * n
    def write(self, b):
        return len(b)

def test_read():
    r = MyRawIO()
    assert r.read(0) == b""
    assert r.read(1) == b"x"
    assert r.read(2) == b"xx"
    assert r.read(3) == b"xxx"
    assert r.read(4) == b"xxxx"
    assert r.read(5) == b"xxxxx"
    assert r.read(6) == b"xxxxxx"
    assert r.read(7) == b"xxxxxxx"
    assert r.read(8) == b"xxxxxxxx"
    assert r.read(9) == b"xxxxxxxxx"
    assert r.read(10) == b"xxxxxxxxxx"
    assert r.read(11) == b"xxxxxxxxxxx"
    assert r.read(12) == b"xxxxxxxxxxxx
