import lzma
# Test LZMADecompressor.__init__()

class TestInit(unittest.TestCase):
    def test_no_args(self):
        d = lzma.LZMADecompressor()
        self.assertEqual(d.format, lzma.FORMAT_AUTO)
        self.assertEqual(d.check, lzma.CHECK_UNKNOWN)
        self.assertEqual(d.filters, None)

    def test_format(self):
        d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
        self.assertEqual(d.format, lzma.FORMAT_XZ)
        self.assertEqual(d.check, lzma.CHECK_UNKNOWN)
        self.assertEqual(d.filters, None)

        d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
        self.assertEqual(d.format, lzma.FORMAT_ALONE)
        self.assertEqual(
