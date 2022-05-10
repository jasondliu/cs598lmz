import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, memlimit=1, filters=[])
decomp.decompress(b"")
decomp.decompress(b"", max_length=1)
# Test LZMADecompressor.read
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
decomp.read(1)
decomp.read()
# Test LZMADecompressor.read1
