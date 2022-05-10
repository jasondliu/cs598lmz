import bz2
# Test BZ2Decompressor
if 'bz2' in __builtins__:
    class BZ2DecompressorTest(unittest.TestCase):
        def test_decompress(self):
            dc = bz2.BZ2Decompressor()
            self.assertRaises(TypeError, dc.decompress, 1)
            self.assertRaises(ValueError, dc.decompress, b'x')
            dc = bz2.BZ2Decompressor()
            self.assertEqual(dc.decompress(bz2.compress(b'1234567890')),
                             b'1234567890')
            dc = bz2.BZ2Decompressor()
            self.assertEqual(dc.decompress(bz2.compress(b'1234567890')),
                             b'1234567890')
            dc.decompress(b'x')
            self.assertEqual(dc.unused_data, b'x')
            dc.decompress(b'x')
            self.assertEqual(
