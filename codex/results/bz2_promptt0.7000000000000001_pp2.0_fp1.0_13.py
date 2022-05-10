import bz2
# Test BZ2Decompressor, BZ2File and BZ2Compressor

class TestBZ2(unittest.TestCase):

    def test_decompressor_type(self):
        self.assertRaises(TypeError, bz2.BZ2Decompressor, 1)

    def test_decompressor(self):
        d = bz2.BZ2Decompressor()
        self.assertRaises(EOFError, d.decompress, b'this is not a valid stream')

        data = bz2.compress(b'ABC' * 100)
        self.assertRaises(ValueError, d.decompress, data, -1)

        self.assertEqual(d.decompress(data, 0), b'')
        self.assertEqual(d.decompress(data), b'ABC' * 100)
        self.assertEqual(d.unused_data, b'')

        self.assertEqual(d.decompress(data + b'garbage'), b'ABC' * 100)
        self.assertEqual(d.
