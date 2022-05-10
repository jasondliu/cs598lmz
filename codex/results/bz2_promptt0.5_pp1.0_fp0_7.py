import bz2
# Test BZ2Decompressor.decompress()

class TestBZ2Decompressor_decompress(TestCase):

    def test_decompress(self):
        for data in [b'', b'BZh91AY&SY', b'BZh91AY&SYA', b'BZh91AY&SY\xaf\x82']:
            bz2_data = bz2.compress(data)
            d = bz2.BZ2Decompressor()
            self.assertEqual(d.decompress(bz2_data), data)
            self.assertEqual(d.decompress(b''), b'')
            self.assertRaises(EOFError, d.decompress, b'BZh91AY&SY')

    def test_unused_data(self):
        bz2_data = bz2.compress(b'x' * 100)
        d = bz2.BZ2Decompressor()
        unused_data = d.decompress(bz2_data, 50)
        self.
