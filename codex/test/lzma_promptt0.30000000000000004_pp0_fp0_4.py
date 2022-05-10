import lzma
# Test LZMADecompressor

# Test decompression of empty stream
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"") == b""

# Test decompression of single-byte stream
decomp = lzma.LZMADecompressor()
