import bz2
# Test BZ2Decompressor for error conditions

class TestBZ2DecompressorErrors(unittest.TestCase):
    # Compressed data with a truncated header
    short_header = b'BZh9\x04\x00\x00\x00\x00\x00\x00\x00\x00'

    def test_truncated_header(self):
        with self.assertRaises(EOFError):
            bz2.decompress(self.short_header)

    # Compressed data with a truncated trailer
    short_trailer = b'BZh9\x04\x00\x00\x00\x00\x00\x00\x00\x00' + (b'A' * 5)

    def test_truncated_trailer(self):
        with self.assertRaises(EOFError):
            bz2.decompress(self.short_trailer)

    # Compressed data with a truncated block header
    short_block_header = b'BZh9\x04\x00\x00
