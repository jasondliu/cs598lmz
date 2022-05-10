import bz2
# Test BZ2Decompressor.eof()

class TestBZ2EOF(unittest.TestCase):
    def test_eof(self):
        for input in ['', 'foo', 'foo' * 100, '\x00' * 100]:
            for compresslevel in xrange(10):
                dc = bz2.BZ2Decompressor()
                c = bz2.BZ2Compressor(compresslevel)
                self.assertFalse(dc.eof)
                self.assertFalse(dc.unused_data)
                self.assertEqual(dc.decompress(c.compress(input)), input)
                self.assertTrue(dc.eof)
                self.assertFalse(dc.unused_data)

    def test_eof_incomplete(self):
        for compresslevel in xrange(10):
            dc = bz2.BZ2Decompressor()
            c = bz2.BZ2Compressor(compresslevel)
            self.assertFalse(dc.eof)
            self.assertFalse(dc.unused_data
