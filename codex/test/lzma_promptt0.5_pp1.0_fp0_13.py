import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
c.decompress(b'\x00')

# Test LZMACompressor
c = lzma.LZMACompressor()
c.compress(b'\x00')
c.flush()

# Test LZMADecompressor.__init__
c = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, filters=None)
