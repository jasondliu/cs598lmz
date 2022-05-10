import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        # Test read(n).
        rawio = io.RawIOBase()
        self.assertRaises(UnsupportedOperation, rawio.read)
        self.assertRaises(UnsupportedOperation, rawio.read, 10)
        # But the argument can be optional.
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b""
        self.assertEqual(MyRawIO().read(), b"")
        # Test read1(n).
        rawio = io.RawIOBase()
        self.assertRaises(UnsupportedOperation, rawio.read1)
        self.assertRaises(UnsupportedOperation, rawio.read1, 10)
        # But the argument can be optional.
        class MyRawIO(io.RawIOBase):
            def read1(self, n=-1):
                return b""
        self.assertEqual(MyRawIO().read1(), b"")
        # Test read
