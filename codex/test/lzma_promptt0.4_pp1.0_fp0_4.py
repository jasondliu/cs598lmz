import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
compressor.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00')

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b'\x00\x00\x00\x00\x00\x00\x00\x00')
compressor.flush()

# Test LZMAFile
