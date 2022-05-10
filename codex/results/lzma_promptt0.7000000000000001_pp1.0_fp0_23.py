import lzma
# Test LZMADecompressor
def test_lzma_decompressor():
    decompress(lzma.decompress, lzma.LZMADecompressor())

# Test LZMADecompressor.decompress
def test_lzma_decompressor_decompress():
    decompress(lzma.decompress, lzma.LZMADecompressor().decompress)

# Test lzma.decompress
def test_lzma_decompress():
    decompress(lzma.decompress)
