import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
comp.decompress(b'\x5d\x00\x00\x80\x00')
# Test LZMACompressor
comp = lzma.LZMACompressor(format=lzma.FORMAT_XZ)
data = comp.compress(b'message') + comp.flush()
data

