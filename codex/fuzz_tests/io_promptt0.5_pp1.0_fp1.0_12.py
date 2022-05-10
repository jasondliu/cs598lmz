import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase
# Test io.IOBase
class TestIoBase(unittest.TestCase):
    class MyRawIO(io.RawIOBase):
        def read(self, size=-1):
            return b"a" * size
        def write(self, b):
            pass
        def seekable(self):
            return True
        def readable(self):
            return True
        def writable(self):
            return True
        def seek(self, pos, whence=0):
            return 0
        def tell(self):
            return 0
        def readall(self):
            return b"a" * 10
        def readinto(self, b):
            b[:10] = b"a" * 10
            return 10
        def truncate(self, size=None):
            return 0
        def close(self):
            pass
    # RawIOBase tests
    def test_read(self):
        self.assertEqual(self.MyRawIO().read(), b"a")
       
