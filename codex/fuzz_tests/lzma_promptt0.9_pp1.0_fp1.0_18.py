import lzma
# Test LZMADecompressor object
compressor = lzma.LZMADecompressor()
uncompressed_data = b""
uncompressed_data += compressor.decompress(b"X" * 10 * 1024 * 1024)
uncompressed_data += compressor.decompress(b"Y" * 10 * 1024 * 1024)
uncompressed_data += compressor.flush()
print(len(uncompressed_data))

# Test Streaming decompression

compressor = lzma.LZMACompressor()
compressed_data = b""
compressed_data += compressor.compress(b"X" * 10 * 1024 * 1024)
compressed_data += compressor.compress(b"Y" * 10 * 1024 * 1024)
compressed_data += compressor.flush()

decompressor = lzma.LZMADecompressor()
uncompressed_data = b""
decompressor.decompress(compressed_data)
uncompressed_data += decompressor.unconsumed_tail
print(len(uncompressed_data))
