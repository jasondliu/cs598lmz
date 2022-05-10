import bz2
# Test BZ2Decompressor.read()

class TestBZ2Read(unittest.TestCase):

    def test_read_method(self):
        # Issue #8141: Check that read() returns the empty string at EOF
        data = bz2.compress(b"some data")
        f = io.BytesIO(data)
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.read(1), b"s")
        self.assertEqual(d.read(1), b"o")
        self.assertEqual(d.read(), b"me data")
        self.assertEqual(d.read(), b"")
        self.assertEqual(d.read(), b"")
        self.assertEqual(d.read(), b"")

    def test_read_method_2(self):
        # Issue #8141: Check that read() returns the empty string at EOF
        data = bz2.compress(b"some data")
        f = io.BytesIO(data)
        d = bz2.
