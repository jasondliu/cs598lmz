import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):
    # Test the RawIOBase implementation.  Note that the
    # tests for readinto() and read() are in test_io.
    # readinto() is implemented in terms of read(),
    # so if read() is correct, readinto() should be correct.

    def test_read(self):
        # Test RawIOBase.read()
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"A")
        self.assertEqual(b.read(2), b"BC")
        self.assertEqual(b.read(3), b"DE")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(1), b"")
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(), b"ABCDE")
        self.assertEqual(b.
