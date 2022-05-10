import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # Test that readinto() returns the correct number of bytes read.
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.readinto, bytearray())
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return super(MyRawIO, self).readinto(b)
        r = MyRawIO()
        self.assertRaises(io.UnsupportedOperation, r.readinto, bytearray())
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return super(MyRawIO, self).readinto(b)
            def read(self, n=-1):
                return b'x' * n
        r = MyRawIO()
        b = bytearray(10)
        self.assertEqual(r.readinto(b), 10)
        self.assertEqual(b, b'xxxxxxxxxx')
