import lzma
# Test LZMADecompressor.decompress() with buffers. 
# This tests for a bug in the C-level LZMA_read() function.
# lzma.LZMADecompressor.decompress() used to be implemented using LZMA_read(). 

input_string = b"ABCDE"

compressed = lzma.compress(input_string)
decomp = lzma.LZMADecompressor()

# For this test we need a very small buffer.
# 4096 bytes is much larger than needed.
buffer_size = 4096

# Split compressed into two parts. Decompress the first part, then the
# second part. Check that the complete decompressed string is correct.

part1, part2 = compressed[:len(compressed)//2], compressed[len(compressed)//2:]

result = b''
