import lzma
# Test LZMADecompressor.test_compat()
test = lzma.LZMADecompressor()


# Test LZMADecompressor.test_readline()
lzdecomp = lzma.LZMADecompressor()
data = b"\x00\x00\x00\x00\x00\x010"
uncompressed = lzdecomp.decompress(data, 9)
assert uncompressed == b"Hello"


# Test LZMACompressor.test_read1()
lzcomp = lzma.LZMACompressor()
uncomp = lzcomp.compress(b"Wonderful, Glorious, LZMA!")
assert uncomp == lzma.LZMACompressor.EOF


# Test LZMACompressor.test_readline()
data = b"eggs\nsausage\ncheese\n"
compressor = lzma.LZMACompressor()
comp_fd = BytesIO()
comp_fd.write(compressor.compress(data))
comp_fd.write(comp
