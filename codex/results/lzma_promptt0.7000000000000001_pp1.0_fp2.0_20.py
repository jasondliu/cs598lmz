import lzma
# Test LZMADecompressor with incremental feed
compressor = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)

with open('foo.xz', 'wb') as f:
    f.write(compressor.compress(b"foo\n"))
    f.write(compressor.compress(b"bar\n"))
    f.write(compressor.compress(b"cheese\n"))
    f.write(compressor.flush())

with lzma.open('foo.xz', format=lzma.FORMAT_ALONE) as f:
    with lzma.open(f, format=lzma.FORMAT_AUTO) as g:
        print(g.read())

os.remove('foo.xz')
# Test LZMADecompressor with multiple filters
compressor = lzma.LZMACompressor(
    filters=[{"id": lzma.FILTER_LZMA2, "preset": 3},
             {"id": lzma.FILTER_DELTA, "dist":
