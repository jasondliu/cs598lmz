import bz2
# Test BZ2Decompressor, BZ2Compressor

class TestBZ2(TestCase):

    def test_BZ2Decompressor(self):
        d = bz2.BZ2Decompressor()
        e = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(bz2data), data)
        self.assertEqual(d.decompress(bz2data[:20]), data[:20])
        self.assertEqual(d.decompress(bz2data[:10]), data[:10])
        self.assertEqual(d.decompress(bz2data[:5]), data[:5])
        self.assertEqual(d.decompress(bz2data), data)
        self.assertEqual(d.decompress(bz2data[20:]), data[20:])
        self.assertEqual(d.decompress(bz2data[30:]), data[30:])
        self.assertEqual(d.decompress(bz2data
