import io
# Test io.RawIOBase
class TestRawIOBase:
    def test_readinto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:4] = b"1234"
                return 4
        b = bytearray(4)
        f = MyRawIO()
        assert f.readinto(b) == 4
        assert b == b"1234"

    def test_readinto_resize(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[0:4] = b"1234"
                return 4
        b = bytearray(5)
        f = MyRawIO()
        assert f.readinto(b) == 4
        assert b == b"1234\x00"
        assert f.readinto(b) == 0
        assert b == b"1234\x00"

