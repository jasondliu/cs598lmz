import lzma
# Test LZMADecompressor

# Test decompression of empty stream
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"") == b""

# Test decompression of single-byte stream
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"\x00") == b"\x00"

# Test decompression of multi-byte stream
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00") == b"\x00" * 8

# Test decompression of multi-byte stream with max_length
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00", max_length=4) == b"\x00" * 4

# Test decompression of multi-byte stream with max_length
dec
