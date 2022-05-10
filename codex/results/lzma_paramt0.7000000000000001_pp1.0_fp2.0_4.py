from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x80I\x01\xe4\x1d\x00\x00\x00')

# decompress
compressor = LZMACompressor()
data = b'Words go here'
compressed = compressor.compress(data)
compressed += compressor.flush()
# compressed now contains the LZMA-compressed data.

decompressor = LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# decompressed now contains the original data.

assert (decompressed == data)

# decompress
compressor = LZMACompressor()
data = b'Words go here'
compressed = compressor.compress(data)
compressed += compressor.flush()
# compressed now contains the LZMA-compressed data.

decompressor = LZMADec
