import bz2
# Test BZ2Decompressor on a list of bytes

class TestBZ2Decompressor(unittest.TestCase):
    def test_decompressor(self):
        d = bz2.BZ2Decompressor()
        self.assertRaises(EofError, d.decompress, b'1')
        self.assertRaises(EofError, d.decompress, b'1'*100)
        self.assertRaises(EofError, d.decompress, b'1'*10000)
        self.assertRaises(EofError, d.decompress, b'1'*1000000)
        self.assertEqual(d.decompress(b'BZh91AY&SY\x04\x00\x00\x00\x00\x00'),
                         b'hello')
        self.assertEqual(d.decompress(b'A'*100), b'')
        self.assertEqual(d.decompress(b'B'*10000), b'')
        self.assertEqual(d.decompress
