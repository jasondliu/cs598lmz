import lzma
# Test LZMADecompressor(format=FORMAT_RAW, memlimit=None, filters=None)

data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
c = lzma.LZMADecompressor()
c.decompress(data)

c = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
c.decompress(data)

c = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
c.decompress(data)

c = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
c.decompress(data)

c = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
c.decompress(data)

# Test LZMADecompressor(format=FORMAT_RAW,
