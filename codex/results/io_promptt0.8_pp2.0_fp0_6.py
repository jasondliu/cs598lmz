import io
# Test io.RawIOBase directly, but can't test io.BytesIO or io.StringIO.
class TestRawIOBase(unittest.TestCase):
    def setUp(self):
        # Derived class with read() and readall() defined
        self.readcount = 0
        class MyBufferedIO(io.RawIOBase):
            def read(self, n=-1):
                if n < 0:
                    return b'abcdefghi' * 3
                else:
                    return (b'abcdefghi' * 3)[:n]
            def readall(self):
                return b'j' * 10000
            def write(self, b):
                pass
        self.mybufio = MyBufferedIO()

    def readtest(self, method, teststring):
        self.readcount += 1
        # test in various chunk sizes
        for size in (1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 63, 64, 65):
            if isinstance(method, str):
                f = getattr(self.mybufio, method)
