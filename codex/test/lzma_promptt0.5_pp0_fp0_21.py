import lzma
# Test LZMADecompressor

# Test decompression of a single byte
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'\x00') == b''
assert decomp.decompress(b'\x00', 1) == b''
assert decomp.decompress(b'\x00', 2) == b''
assert decomp.decompress(b'\x00', 3) == b''
assert decomp.decompress(b'\x00', 4) == b''
assert decomp.decompress(b'\x00', 5) == b''
assert decomp.decompress(b'\x00', 6) == b''
assert decomp.decompress(b'\x00', 7) == b''
assert decomp.decompress(b'\x00', 8) == b''

# Test decompression of a single block
decomp = lzma.LZMADecompressor()
