import lzma
# Test LZMADecompressor and LZMACompressor

# Create a test string
test_string = b'1234567890' * 100000

# Compress the test string
compressor = lzma.LZMACompressor()
compressed_string = compressor.compress(test_string)
compressed_string += compressor.flush()

# Decompress the compressed string
decompressor = lzma.LZMADecompressor()
decompressed_string = decompressor.decompress(compressed_string)

# Check that the decompressed string matches the original
assert decompressed_string == test_string

# Check that the decompressor is exhausted
assert decompressor.eof

# Check that the decompressor can handle multiple streams
