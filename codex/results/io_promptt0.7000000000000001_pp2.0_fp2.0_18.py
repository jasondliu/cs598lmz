import io
# Test io.RawIOBase class.
#
# This is tested in the regression tests by test_io.
#
# Issue #16085: io.RawIOBase.readinto() should return how many bytes have
# been read.

class RawIOTest(unittest.TestCase):
    def test_readinto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'1234567890'
                return len(b)
        f = MyRawIO()
        b = bytearray(5)
        n = f.readinto(b)
        self.assertEqual(n, 5)
        self.assertEqual(b, b'12345')
        b = bytearray(10)
        n = f.readinto(b)
        self.assertEqual(n, 10)
        self.assertEqual(b, b'1234567890')

# Test io.BufferedIOBase class.
#
# This is tested in the regression tests by test_io.
#

