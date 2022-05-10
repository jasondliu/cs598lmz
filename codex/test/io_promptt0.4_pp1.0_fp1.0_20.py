import io
# Test io.RawIOBase

class TestRawIOBase:
    def test_read_into(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        t = TestRawIO()
        b = bytearray(10)
        assert t.readinto(b) == 0
        assert len(b) == 10
        assert t.readinto(b) == 0
        assert len(b) == 10

    def test_readinto_resize(self):
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b.append(0)
                return 1
        t = TestRawIO()
        b = bytearray(10)
        assert t.readinto(b) == 1
        assert len(b) == 11
        assert t.readinto(b) == 1
        assert len(b) == 12

