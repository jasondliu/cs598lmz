import lzma
# Test LZMADecompressor objects

def test_LZMADecompressor():
    # Test the LZMADecompressor class.

    def decompress(compressor, data):
        # Decompress data using the given compressor, but only decompress as
        # much as possible.
        try:
            return compressor.decompress(data, 0)
        except EOFError:
            return compressor.unconsumed_tail

    # Test decompression.

    empty_block = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00'
    uncompressed_data = b"".join([b"foo", empty_block, b"bar"])

    compression_params = lzma.FORMAT_RAW, lzma.FILTER_LZMA1, lzma.CHECK_NONE
    compressed_data = lzma.compress(uncompressed_data, *compression_params)
