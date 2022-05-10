import io
# Test io.RawIOBase


class RawIOBaseTest(unittest.TestCase):

    class MockRawIO(io.RawIOBase):

        def readable(self):
            return True

        def writable(self):
            return True

        def seekable(self):
            return True

        def readinto(self, b):
            return 0

        def write(self, b):
            return 0

        def seek(self, pos, whence=0):
            return 0

        def tell(self):
            return 0

        def read(self, n=-1):
            return b''

        def readall(self):
            return b''

        def close(self):
            pass
    f = MockRawIO()
    for attr in ('read', 'readinto', 'write', 'seek', 'tell', 'close'):
        meth = getattr(f, attr)
        self.assertRaises(io.UnsupportedOperation, meth)
    self.assertEqual(f.mode, 'wb+')
    self.assertRaises(io.UnsupportedOperation, io.RawIOBase,
