import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):
    def test_args(self):
        # Issue #19073: check that RawIOBase.read() and .write() accepts
        # the same arguments as their IOBase counterpart.
        class MyRawIO(io.RawIOBase):
            def writable(self):
                return False
            def readable(self):
                return True
            def close(self):
                pass
            def seekable(self):
                return False

            def readinto(self, buf):
                return len(buf)
            def read(self, n=-1):
                return b"0" * n

            def write(self, b):
                raise NotImplementedError

        myio = MyRawIO()
        self.assertEqual(myio.read(), b"")
        self.assertEqual(myio.read(10), b"0000000000")
        self.assertEqual(myio.read(0), b"")
        self.assertEqual(myio.read(None), b"")
        self
