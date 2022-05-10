import lzma
# Test LZMADecompressor

def test_lzma_compress():
    for text in texts:
        for level in range(2, 3):
            # LZMA compression
            compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ,
                                            check=lzma.CHECK_CRC64,
                                            preset=level)
            compressed = compressor.compress(text)
            compressed += compressor.flush()
            # LZMA decompression
            decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ,
                                                 check=lzma.CHECK_CRC64)
            decompressed = decompressor.decompress(compressed)
            # Check
            assert decompressed == text

