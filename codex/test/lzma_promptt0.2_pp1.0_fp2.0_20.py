import lzma
# Test LZMADecompressor

# Test empty input
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'') == b''

# Test decompression of a single byte
decomp = lzma.LZMADecompressor()
