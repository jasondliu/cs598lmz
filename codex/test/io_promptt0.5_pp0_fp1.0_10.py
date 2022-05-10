import io
# Test io.RawIOBase

class TestRawIOBase:
    def test_read(self):
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"xyz"
        with TestRawIO() as t:
            assert t.read() == b"xyz"
            assert t.read(None) == b"xyz"
            assert t.read(2) == b"xy"
            assert t.read(4) == b"z"
            assert t.read(1) == b""
            assert t.read(0) == b""
            assert t.read(-1) == b"xyz"
            assert t.read(-2) == b"xyz"
            assert t.read() == b""
            assert t.read(1) == b""

    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b"xyz"
