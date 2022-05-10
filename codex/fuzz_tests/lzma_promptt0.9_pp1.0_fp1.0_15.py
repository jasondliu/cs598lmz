import lzma
# Test LZMADecompressor(format=FORMAT_AUTO)
d = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
assert d.format == lzma.FORMAT_XZ
assert d.check is None
# Test LZMADecompressor(format=FORMAT_XZ)
d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
assert d.format == lzma.FORMAT_XZ
assert d.check == lzma.CHECK_CRC64
# Test LZMADecompressor(format=FORMAT_ALONE)
d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
assert d.format == lzma.FORMAT_ALONE
assert d.check is None
# Test LZMADecompressor(format=FORMAT_RAW)
d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
assert d.format == lzma.
