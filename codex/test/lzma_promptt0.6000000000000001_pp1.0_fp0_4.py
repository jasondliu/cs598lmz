import lzma
# Test LZMADecompressor
l = lzma.LZMADecompressor()
l.decompress(b'\x00\x00\x00\x00')

# Test LZMACompressor
l = lzma.LZMACompressor()
l.compress(b'\x00\x00\x00\x00')

# Test LZMAFile
