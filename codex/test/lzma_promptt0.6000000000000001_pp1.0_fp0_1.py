import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\x00\x00')

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b'Hello') + compressor.flush()

# Test BZ2Compressor
