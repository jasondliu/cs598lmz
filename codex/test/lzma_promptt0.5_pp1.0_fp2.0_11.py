import lzma
# Test LZMADecompressor

import lzma

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"some data"

compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.decompress() with a truncated file

import lzma

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"some data"

compressed = compressor.compress(data)
compressed += compressor.flush()

# Truncate the compressed data
compressed = compressed[:-5]

# This will raise an EOFError, because the input is too short
decompressed = decompressor.decompress(compressed)

print(decompressed)
# Test LZMADecompressor.decompress() with a truncated
