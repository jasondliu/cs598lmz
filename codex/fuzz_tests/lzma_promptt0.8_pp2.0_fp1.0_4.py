import lzma
# Test LZMADecompressor and LZMACompressor

# Since LZMADecompressor and LZMACompressor inherit from
# StreamingBuffer, we can test them using the streaming API.

# We use LZMADecompressor because it is easier to build a valid LZMA
# stream with LZMADecompressor.

# Test LZMADecompressor

# Writes decompressed data to memory buffer
output_buf = []

# Feed LZMADecompressor a valid LZMA stream
lzma_decompressor = lzma.LZMADecompressor()
lzma_decompressor.decompress_to(output_buf, b"\x5d\x00\x00\x80\x00")

# Calling decompress_to without data will flush the decompressor
lzma_decompressor.decompress_to(output_buf)

# Check decompressed data
assert b"".join(output_buf) == b"test data"

# Test LZMACompressor

# Create an LZMACompressor instance
