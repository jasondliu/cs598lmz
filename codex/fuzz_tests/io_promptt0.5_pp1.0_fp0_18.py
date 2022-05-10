import io
# Test io.RawIOBase.read()

class TestRawIOBaseRead(unittest.TestCase):
    def test_read_0(self):
        # Test reading 0 bytes
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b''
        r = TestRawIO()
        self.assertEqual(r.read(), b'')
        self.assertEqual(r.read(0), b'')
        self.assertEqual(r.read(1), b'')
        self.assertEqual(r.read1(0), b'')
        self.assertEqual(r.read1(1), b'')
        self.assertEqual(r.readinto(bytearray()), 0)
        self.assertEqual(r.readinto(bytearray(1)), 0)

    def test_read_1(self):
        # Test reading 1 byte
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'x'
        r =
