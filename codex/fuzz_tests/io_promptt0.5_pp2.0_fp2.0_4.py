import io
# Test io.RawIOBase
class TestRawIOBase:
    def test_readinto(self):
        b = bytearray(b"abc")
        r = io.BytesIO(b"def")
        n = r.readinto(b)
        assert n == 3
        assert b == b"def"
        n = r.readinto(b)
        assert n == 0
        assert b == b"def"
        r = io.BytesIO(b"abcdef")
        n = r.readinto(b, 1)
        assert n == 3
        assert b == b"adcdef"
        n = r.readinto(b, 3)
        assert n == 3
        assert b == b"adcd"
        n = r.readinto(b, 6)
        assert n == 0
        assert b == b"adcd"
        raises(TypeError, r.readinto)
        raises(TypeError, r.readinto, None)
        raises(TypeError, r.readinto, "abc")
        raises(TypeError, r.readinto, b"abc")

