import lzma
# Test LZMADecompressor()
c = lzma.LZMADecompressor()
c.decompress(b'YXG')

# Test LZMACompressor()
c = lzma.LZMACompressor()
c.compress(b'QWERTYUI')
c.flush()
