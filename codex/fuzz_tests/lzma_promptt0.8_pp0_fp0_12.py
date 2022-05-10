import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
decompressed_data = compressor.decompress(compressed_data)

print(decompressed_data)
 

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(b"witch which has which witches wrist watch")
compressed_data += compressor.flush()

print(compressed_data)

# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
decompressed_data = compressor.decompress(compressed_data)

print(decompressed_data)
 

# Test LZMACompressor
compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ)
compressed_data = compressor.compress(b"witch which has which witches wrist watch")
compressed_data += compressor.flush()

print(compressed_data)

# Test LZMADecompressor
compressor =
