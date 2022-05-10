import lzma
# Test LZMADecompressor
assert lzma.LZMADecompressor().decompress(compressed) == raw_data
# Compress and decompress in one step
assert lzma.decompress(compressed) == raw_data

# Test with a block size of 1
for block_size in (None, 1):
    compressor = lzma.LZMACompressor(block_size)
    compressor.compress(bytes(1))
    compressor.compress(bytes(2))
    compressed = compressor.flush()
    assert lzma.decompress(compressed) == bytes((1, 2))

# Test with a block size of 2
compressor = lzma.LZMACompressor(block_size=2)
compressor.compress(bytes(7))
compressor.compress(bytes(1))
compressed = compressor.flush()

assert lzma.decompress(compressed) == bytes((7, 0))

# Make sure we use the same 'dict_size' value as the reference
# implementation (when no dictionary is explicitly set).
for dictionary_
