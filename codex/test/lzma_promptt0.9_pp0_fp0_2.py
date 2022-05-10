import lzma
# Test LZMADecompressor.test_compat()
test = lzma.LZMADecompressor()


# Test LZMADecompressor.test_readline()
lzdecomp = lzma.LZMADecompressor()
data = b"\x00\x00\x00\x00\x00\x010"
uncompressed = lzdecomp.decompress(data, 9)
