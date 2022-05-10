import lzma
# Test LZMADecompressor
class LZMADecompressorTest(LZMATest):
    compressor = lzma.LZMACompressor
    decompressor = lzma.LZMADecompressor

    def test_decompressor(self):
        with self.assertRaises(lzma.LZMAError) as cm:
            self.decompressor().decompress(b'foo')
        self.assertEqual(cm.exception.errno, lzma.LZMAError.BUF_ERROR)
        with self.assertRaises(lzma.LZMAError) as cm:
            self.decompressor().decompress(self.empty_compressed)
        self.assertEqual(cm.exception.errno, lzma.LZMAError.DATA_ERROR)

        # LZMA header is present.
        with self.assertRaises(lzma.LZMAError) as cm:
            self.decompressor().decompress(self.compressed_with_empty_header)
        self.assertEqual(cm.
