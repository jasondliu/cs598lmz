import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
decompressor.decompress(data)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b'foo')
compressor.flush()

# Test LZMADecompressor.decompress
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Test LZMADecompressor.decompress_chunk
decompressor = lzma.LZMADecompressor()
