import lzma
# Test LZMADecompressor

# TODO: Test with a large input file

class TestLZMADecompressor(unittest.TestCase):

    def test_decompress(self):
        # Test that calling decompress() raises an exception
        # when the input is empty
        decompressor = lzma.LZMADecompressor()
        self.assertRaises(EOFError, decompressor.decompress, b'')

    def test_flush(self):
        # Test that calling flush() raises an exception
        # when the input is empty
        decompressor = lzma.LZMADecompressor()
        self.assertRaises(EOFError, decompressor.flush)

    def test_unused_data(self):
        # Test that unused_data is empty when the input is empty
        decompressor = lzma.LZMADecompressor()
        self.assertEqual(decompressor.unused_data, b'')

    def test_decompress_with_large_bufsize(self):
        # Issue #13761: decompress
