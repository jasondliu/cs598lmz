import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:] = b'foo'
                return 3
        r = MyRawIO()
        self.assertEqual(r.read(5), b'foo')
        self.assertEqual(r.read(), b'')
        self.assertEqual(r.readinto(bytearray(5)), 3)
        self.assertEqual(r.readinto(bytearray(5)), 0)
        self.assertEqual(r.readinto(bytearray(5)), 0)
        self.assertEqual(r.readinto(bytearray(5)), 0)
        self.assertEqual(r.readinto(bytearray(5)), 0)
        self.assertEqual(r.readinto(bytearray(5)), 0)
        self.assertEqual(r.read
