import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(b'\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00')
# Test LZMACompressor
comp = lzma.LZMACompressor()
comp.compress(b'foo')
comp.flush()

# Test LZMAFile
