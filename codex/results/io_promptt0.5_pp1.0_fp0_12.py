import io
# Test io.RawIOBase
class TestRawIOBase(BaseTestIOBase):
    def test_read(self):
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'\x00' * n
        f = TestRawIO()
        self.assertEqual(f.read(0), b'')
        self.assertEqual(f.read(10), b'\x00' * 10)
        self.assertEqual(f.read(), b'\x00' * -1)
        self.assertEqual(f.read(), b'')
        f.close()
        self.assertRaises(ValueError, f.read)
        self.assertRaises(ValueError, f.read, 10)
        self.assertRaises(ValueError, f.read, 0)
        self.assertRaises(ValueError, f.read, -1)
    def test_readall(self):
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'\x
