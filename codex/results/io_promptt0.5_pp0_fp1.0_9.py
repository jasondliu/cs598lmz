import io
# Test io.RawIOBase

import _io

class TestRawIOBase(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

def test_readinto():
    r = TestRawIOBase()
    b = bytearray(5)
    assert r.readinto(b) == 3
    assert b == b"fooba"

def test_readinto_resize():
    r = TestRawIOBase()
    b = bytearray(2)
    assert r.readinto(b) == 3
    assert b == b"foob"

def test_readinto_readall():
    r = TestRawIOBase()
    b = bytearray(2)
    assert r.readinto(b) == 3
    assert r.readinto(b) == 0

def test_readinto_no_resize():
    r = TestRawIOBase()
    b = bytearray(2)
    assert r.readinto(b, resize=False) == 2
    assert
