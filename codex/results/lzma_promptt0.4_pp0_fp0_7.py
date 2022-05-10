import lzma
# Test LZMADecompressor
class TestLZMADecompressor(unittest.TestCase):
    def test_decompress(self):
        cdata = lzma.compress(b"foo")
        d = lzma.LZMADecompressor()
        self.assertEqual(d.decompress(cdata), b"foo")
        self.assertEqual(d.flush(), b"")
        self.assertEqual(d.decompress(b""), b"")
        self.assertEqual(d.flush(), b"")
        self.assertRaises(EOFError, d.decompress, b"a")
        self.assertRaises(ValueError, d.decompress, b"foo")
        self.assertRaises(ValueError, d.decompress, cdata + b"a")
        self.assertRaises(ValueError, d.decompress, cdata[:-1])
        self.assertRaises(ValueError, d.decompress, cdata[:-1], 1)
        self.assertRaises(Value
