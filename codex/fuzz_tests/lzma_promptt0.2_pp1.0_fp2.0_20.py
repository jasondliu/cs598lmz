import lzma
# Test LZMADecompressor

# Test empty input
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'') == b''

# Test decompression of a single byte
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'\x00') == b'\x00'

# Test decompression of a single block
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
