import io
# Test io.RawIOBase()

class TestRawIOBase:

    def test_readinto(self):
        # readinto()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:] = b"hello world"[:len(b)]
                return len(b)

        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        assert n == 5
        assert buf == b"hello"
        assert type(buf) == type(bytearray(b""))

        f = TestRawIO()
        n = f.readinto(memoryview(buf))
        assert n == 5
        assert buf == b"hello"
        assert type(buf) == type(bytearray(b""))

        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf, 3)
        assert n == 2
        assert buf == b"\x00\x00hel"
       
