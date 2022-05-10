import lzma
# Test LZMADecompressor

compressed = lzma.compress(b'This is a test')
compressed

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

decompressor.unused_data

decompressor.decompress(decompressor.unused_data)

decompressor.unused_data

# Test LZMADecompressor with multiple concatenated streams

compressed = lzma.compress(b'This is a test')
compressed += lzma.compress(b'This is a test')

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

decompressor.unused_data

decompressor.decompress(decompressor.unused_data)

decompressor.unused_data

# Test LZMADecompressor.flush()

compressed = lzma.compress(b'This is a test')

decompressor = lzma
