import lzma
# Test LZMADecompressor, LZMAInputFile, LZMAError
import unittest
from os import path

class LZMADecompressorTestCase(unittest.TestCase):

    def test_LZMADecompressor(self):
        # Encode some data
        compressor = lzma.LZMACompressor()
        data = b"".join(compressor.compress(b"abc") for i in range(10))
        data += compressor.flush()
        # Decode data with incremental decoder
        decoder = lzma.LZMADecompressor()
        self.assertTrue(decoder.needs_input)
        output = decoder.decompress(data)
        self.assertTrue(decoder.needs_input)
        self.assertEqual(output, b"abc" * 10)
        decoder.reset()
        # Decode data with multiple calls to decompress()
        decoder = lzma.LZMADecompressor()
        output = b""
        while True:
            chunk = decoder.decompress(data
