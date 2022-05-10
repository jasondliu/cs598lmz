import lzma
# Test LZMADecompressor
class TestLZMADecompressor(unittest.TestCase):
    def test_decompression(self):
        with lzma.open(TESTFN, "rb",
                       format=lzma.FORMAT_XZ,
                       filters=[{"id": lzma.FILTER_LZMA1,
                                 "dict_size": 2**16,
                                 "lc": 3, "lp": 0, "pb": 2,
                                 "mode": lzma.MODE_NORMAL}]) as f:
            with io.open(TESTFN + "_uncompressed", "wb") as o:
                o.write(f.read())
        self.assertFalse(os.path.exists(TESTFN))
        self.assertTrue(filecmp.cmp(TESTFN + "_uncompressed",
                                    TESTFN + "_compressed",
                                    shallow=False))

    def test_invalid_options(self):
        self.assertRaises(ValueError,
                          lzma.LZMADecompressor, format=l
