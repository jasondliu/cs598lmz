import lzma
# Test LZMADecompressor object
src_data = b'witch which has which witches wrist watch'
compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(src_data)
compressed_data += compressor.flush()
print(compressed_data)

# Test LZMADecompressor object
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(compressed_data))

# Test LZMADecompressor with decompress() function
print(lzma.decompress(compressed_data))
