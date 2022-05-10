import lzma
# Test LZMADecompressor.decompress() with a large chunk size.
# The chunk size is larger than the size of the input data,
# so the input data must be returned in a single call.

input_data = b"Hello, world!"

compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(input_data)
compressor.flush()

decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(compressed_data, 1<<30) == input_data
# Test LZMADecompressor.decompress() with a small chunk size.
# The input data is larger than the chunk size, so the input
# data must be returned in several calls.

input_data = b"Hello, world!"

compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(input_data)
compressor.flush()

decompressor = lzma.LZMADecompressor()

output_data = b""
while True:
    chunk =
