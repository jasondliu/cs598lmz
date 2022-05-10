import io
# Test io.RawIOBase

class TestRawIOBase:

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xy"
        rawio = TestRawIO()
        assert rawio.read() == b"xy"
        assert rawio.read(0) == b""
        assert rawio.read(-1) == b"xy"
        assert rawio.read(1) == b"x"
        assert rawio.read(2) == b"y"
        assert rawio.read(3) == b"y"

    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:2] = b"xy"
                return 2
        rawio = TestRawIO()
        b = bytearray(3)
        assert rawio.readinto(b) == 2
        assert b == b"xy\
