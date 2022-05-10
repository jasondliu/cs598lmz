import io
# Test io.RawIOBase
class TestRawIOBase:
    def test_readinto(self):
        class TestRawIOWrapper(io.RawIOBase):
            def __init__(self):
                self.pos = 0
            def readable(self):
                return True
            def readinto(self, b):
                n = min(len(b), 4 - self.pos)
                for i in range(n):
                    b[i] = i + self.pos
                self.pos = min(4, self.pos + len(b))
                return n
        f = TestRawIOWrapper()
        a = bytearray(3)
        n = f.readinto(a)
        assert n == 3
        assert a == (0, 1, 2)
        a = bytearray(10)
        n = f.readinto(a)
        assert n == 1
        assert a[0] == 3
        assert a[1] == 0
        a = bytearray(2)
        n = f.readinto(a)
        assert n == 0

