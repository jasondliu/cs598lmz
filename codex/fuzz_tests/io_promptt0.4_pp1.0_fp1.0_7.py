import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'x'*n
        rawio = TestRawIO()
        self.assertEqual(rawio.read(0), b'')
        self.assertEqual(rawio.read(5), b'xxxxx')
        self.assertEqual(rawio.read(), b'x'*io.DEFAULT_BUFFER_SIZE)
        self.assertRaises(TypeError, rawio.read, 'foo')
        self.assertRaises(ValueError, rawio.read, -2)
        # Make sure self.read() is not called for zero-sized reads
        class ZeroSizedRawIO(io.RawIOBase):
            def read(self, n=-1):
                raise AssertionError
        rawio = ZeroSizedRawIO()
        self.assertEqual(rawio.read(0),
