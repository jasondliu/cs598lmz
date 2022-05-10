import lzma
# Test LZMADecompressor

# Test that the decompressor can handle a single-byte input
d = lzma.LZMADecompressor()
assert d.decompress(b"\x00") == b""

# Test that the decompressor can handle a single-byte input with a dictionary
d = lzma.LZMADecompressor(lzma.FORMAT_RAW, None, lzma.FILTER_LZMA1,
                          filters=[{"id": lzma.FILTER_DELTA, "dist": 1}])
assert d.decompress(b"\x00") == b""

# Test that the decompressor can handle a single-byte input with a preset
d = lzma.LZMADecompressor(preset=9)
assert d.decompress(b"\x00") == b""

# Test that the decompressor can handle a single-byte input with a preset
# and a dictionary
d = lzma.LZMADecompressor(preset=9, filters=[{"id": lzma.FILTER_D
