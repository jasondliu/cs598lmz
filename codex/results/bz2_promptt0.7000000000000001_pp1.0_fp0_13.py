import bz2
# Test BZ2Decompressor

class BZ2DecompressorTestCase(unittest.TestCase):
    def test_decompressor_simple(self):
        # Decompress a string
        comp = bz2.compress('hello world')
        self.assertEqual(b'hello world', bz2.decompress(comp))

    def test_decompressor_type_error(self):
        # Decompressor objects only work on bytes
        d = bz2.BZ2Decompressor()
        self.assertRaises(TypeError, d.decompress, 'junk')

    def test_decompressor_decompress(self):
        # Feed decompressor some data in chunks
        comp = bz2.compress('hello world')
        d = bz2.BZ2Decompressor()
        d.decompress(comp[0:5])
        d.decompress(comp[5:10])
        self.assertEqual(b'hello world', d.decompress(comp[10:]))

    def test_decompressor_non_
