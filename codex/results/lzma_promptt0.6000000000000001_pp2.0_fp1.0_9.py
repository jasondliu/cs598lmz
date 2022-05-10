import lzma
# Test LZMADecompressor

from lzma import LZMADecompressor
from io import BytesIO


def test_lzma_decompressor_works_after_eof():
    decompressor = LZMADecompressor()
    data = b"x" * 1000000
    compressed = lzma.compress(data)
    # Feed the whole string at once.
    decompressor.decompress(compressed)
    # This shouldn't raise any exception.
    decompressor.flush()
    # Now feed one byte at a time.
    decompressor = LZMADecompressor()
    for i in range(0, len(compressed), 2):
        decompressor.decompress(compressed[i:i+1])
    # This shouldn't raise any exception.
    decompressor.flush()
    # Now feed one byte, then request one byte.
    decompressor = LZMADecompressor()
    for i in range(0, len(compressed), 2):
        decompressor.decompress(compressed[i:i+1])
        decompressor
