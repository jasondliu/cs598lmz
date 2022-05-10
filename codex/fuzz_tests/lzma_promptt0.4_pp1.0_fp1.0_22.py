import lzma
# Test LZMADecompressor.read()

class TestLZMADecompressorRead(unittest.TestCase):
    def test_read(self):
        for level in range(0, 9):
            with open(TESTFN, "wb") as f:
                f.write(b"foo" * 100000)
            with open(TESTFN, "rb") as f:
                cdata = lzma.compress(f.read(), format=lzma.FORMAT_XZ,
                                      check=-1, preset=level)
            with lzma.LZMADecompressor() as d:
                self.assertEqual(d.read(1), b"")
                self.assertEqual(d.read(1), b"")
                self.assertEqual(d.read(1), b"")
                self.assertEqual(d.read(1), b"")
                self.assertEqual(d.read(10000), b"")
                self.assertEqual(d.read(1), b"")
                self.assertEqual(d.
