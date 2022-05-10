import lzma
# Test LZMADecompressor
#

class TestLZMADecompressor(unittest.TestCase):
    def test_decompressor(self):
        with open(TESTFN, "wb") as fp:
            fp.write(lzma.compress(b"Hello!"))

        with open(TESTFN, "rb") as fp:
            with lzma.open(fp, "rb") as xfp:
                data = xfp.read()
        self.assertEqual(data, b"Hello!")

        decomp = lzma.LZMADecompressor()
        with open(TESTFN, "rb") as fp:
            with lzma.open(fp, "rb") as xfp:
                data = decomp.decompress(xfp.read())
        self.assertEqual(data, b"Hello!")
        data = decomp.decompress()
        self.assertEqual(data, b"")
        data = decomp.decompress(b"")
        self.assertEqual(data, b"")

       
