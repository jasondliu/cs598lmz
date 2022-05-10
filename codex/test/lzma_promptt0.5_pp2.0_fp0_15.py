import lzma
# Test LZMADecompressor.

def test_LZMADecompressor(size=128, blocksize=16):
    c = lzma.LZMADecompressor()
    d = lzma.LZMADecompressor()

    s = b"".join(block * blocksize for block in map(chr, range(256)))
    s = s[:size]

    for level in range(1, 9):
        c.compress(s)
        compressed = c.flush()
        decompressed = d.decompress(compressed)
        assert decompressed == s

def test_LZMADecompressor_with_filters():
    c = lzma.LZMACompressor(
        filters=[{"id": lzma.FILTER_LZMA2, "preset": 0}])
    d = lzma.LZMADecompressor(
        filters=[{"id": lzma.FILTER_LZMA2, "preset": 0}])

