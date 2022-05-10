import bz2
# Test BZ2Decompressor
class TestBZ2Decompressor(TestBZ2Compressor):
    def setUp(self):
        self.c = bz2.BZ2Decompressor()
        self.need_eof_marker = False
    def test_compress_decompress(self):
        # Test with a file as input
        datafile = open(test_support.TESTFN, "wb")
        try:
            for n in range(1, 1002):
                datafile.write(S * n)
            datafile.close()
            datafile = open(test_support.TESTFN, "rb")
            c = bz2.BZ2Compressor()
            dc = bz2.BZ2Decompressor()
            while 1:
                datum = datafile.read(1000)
                if not datum:
                    break
                cdatum = c.compress(datum)
                if cdatum:
                    self.assertEqual(dc.decompress(cdatum), datum)
                else:
                    self.assertEqual
