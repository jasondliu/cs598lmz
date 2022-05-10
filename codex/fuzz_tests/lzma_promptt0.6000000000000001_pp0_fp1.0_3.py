import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()

compressor.decompress(b'XZ\xfd\x37\x7a\x58\x5a\x00')

compressor.decompress(b'\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01')

compressor.flush()

# Test LZMACompressor
compressor = lzma.LZMACompressor()

compressor.compress(b'hello world')

compressor.flush()

# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()

decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00!\x15\x00\x00\x00\x00')

decompressor.flush()

# Test decompress().
