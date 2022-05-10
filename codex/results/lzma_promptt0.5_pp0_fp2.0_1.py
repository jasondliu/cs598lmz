import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
compressor.compress(b"hello")
compressor.compress(b"world")
compressor.flush()
data = compressor.compress(b"hello")
data += compressor.flush()
data
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)
decompressor.decompress(b"world")
decompressor.flush()
# Test LZMADecompressor.decompress
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
decompressor.decompress(b"\x00\x00\
