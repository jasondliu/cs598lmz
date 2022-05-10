import io
# Test io.RawIOBase

class TestRawIOBase:

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xy"
        rawio = TestRawIO()
        assert rawio.read(2) == b"xy"
        assert rawio.read(1) == b""
        assert rawio.read() == b""

    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:2] = b"xy"
                return 2
        rawio = TestRawIO()
        b = bytearray(5)
        assert rawio.readinto(b) == 2
        assert b == b"xy\x00\x00\x00"
        assert rawio.readinto(b) == 0
        assert b == b"xy\x00\x00\x00"

    def test_readall
