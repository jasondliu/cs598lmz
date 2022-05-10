import lzma
# Test LZMADecompressor.

# Test with empty data.
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"") == b""
assert decomp.unused_data == b""
assert decomp.eof is False
assert decomp.decompress(b"") == b""
assert decomp.unused_data == b""
assert decomp.eof is False

# Test with a single byte.
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"\x00") == b""
assert decomp.unused_data == b"\x00"
assert decomp.eof is False
assert decomp.decompress(b"\x00") == b""
assert decomp.unused_data == b"\x00"
assert decomp.eof is False

# Test with a single byte, but with two calls to decompress().
decomp = lzma.LZMADecompressor()
assert decomp.decompress(b"\x00") == b""
assert decomp.unused_data == b
