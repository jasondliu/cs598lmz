import io
# Test io.RawIOBase

import io

class TestRawIOBase:

    def test_read(self):
        # read()
        b = io.BytesIO(b"abc")
        assert b.read() == b"abc"
        assert b.read() == b""
        b = io.BytesIO(b"abc")
        assert b.read(None) == b"abc"
        b = io.BytesIO(b"abc")
        assert b.read(2) == b"ab"
        b = io.BytesIO(b"abc")
        assert b.read(4) == b"abc"
        b = io.BytesIO(b"abc")
        assert b.read(0) == b""
        raises(TypeError, b.read, "xyz")

    def test_readinto(self):
        # readinto()
        b = io.BytesIO(b"abcde")
        bf = io.BufferedReader(b)
        a = bytearray(b"xxxxx")
        n = bf.readinto(a)
        assert n
