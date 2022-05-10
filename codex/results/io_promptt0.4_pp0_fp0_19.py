import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test reading
        with open(support.TESTFN, "wb") as f:
            f.write(b"abc")
        with open(support.TESTFN, "rb") as f:
            rawio = io.RawIOBase(f)
            self.assertEqual(rawio.read(1), b"a")
            self.assertEqual(rawio.read(1), b"b")
            self.assertEqual(rawio.read(1), b"c")
            self.assertEqual(rawio.read(1), b"")
            self.assertEqual(rawio.read(1), b"")
        with open(support.TESTFN, "rb") as f:
            rawio = io.RawIOBase(f)
            self.assertEqual(rawio.read(2), b"ab")
            self.assertEqual(rawio.read(2), b"c")
            self.assertEqual(raw
