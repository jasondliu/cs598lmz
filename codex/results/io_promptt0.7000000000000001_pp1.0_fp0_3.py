import io
# Test io.RawIOBase
class RawIO_Test(unittest.TestCase):
    def test_ctor(self):
        def f(self, *args, **kwargs):
            return io.RawIOBase.__init__(self, *args, **kwargs)
        self.assertRaises(NotImplementedError, f, io.RawIOBase())
    def test_read(self):
        def f(self, *args, **kwargs):
            return io.RawIOBase.read(self, *args, **kwargs)
        self.assertRaises(NotImplementedError, f, io.RawIOBase())
    def test_readinto(self):
        def f(self, *args, **kwargs):
            return io.RawIOBase.readinto(self, *args, **kwargs)
        self.assertRaises(NotImplementedError, f, io.RawIOBase())
    def test_readall(self):
        def f(self, *args, **kwargs):
            return io.RawIOBase.readall(self, *args, **
