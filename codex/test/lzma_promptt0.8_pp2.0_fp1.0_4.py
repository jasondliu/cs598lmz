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
