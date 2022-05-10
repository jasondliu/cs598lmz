import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        # Test that read() calls readinto()
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                for i in range(len(b)):
                    b[i] = i
                return len(b)
        r = MyRawIO()
        self.assertEqual(r.read(), b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')
        self.assertEqual(r.read(10), b'')
        self.assertEqual(r.readinto(bytearray(10)), 0)
        self.assertEqual(r.readinto(bytearray(10)), 0)
        self.assertEqual(r.read(10), b'')
        self.assertEqual(r.readinto(bytearray(10)), 0)

    def test_readall(self):
        # Test that readall() calls
