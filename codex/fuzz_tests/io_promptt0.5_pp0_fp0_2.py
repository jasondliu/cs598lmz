import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        # Issue #19056: io.RawIOBase.readinto() should work with bytearray
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'\x01\x02\x03'
                return len(b)

        b = bytearray(3)
        n = MyRawIO().readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'\x01\x02\x03')

    def test_readinto_array(self):
        # Issue #19056: io.RawIOBase.readinto() should work with array.array
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = array.array('B', b'\x01\x02\x03')
                return len(b)

        b
