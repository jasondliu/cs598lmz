import lzma
# Test LZMADecompressor with incremental feed
compressor = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)

with open('foo.xz', 'wb') as f:
    f.write(compressor.compress(b"foo\n"))
    f.write(compressor.compress(b"bar\n"))
    f.write(compressor.compress(b"cheese\n"))
    f.write(compressor.flush())

