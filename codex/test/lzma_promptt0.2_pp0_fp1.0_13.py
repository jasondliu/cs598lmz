import lzma
# Test LZMADecompressor

# Test decompression of empty data
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'') == b''
assert decomp.unused_data == b''
assert decomp.eof == False

# Test decompression of a single byte
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b'\x00') == b''
