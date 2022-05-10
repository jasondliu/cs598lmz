import lzma
# Test LZMADecompressor.flush()

# Check that flush() returns an empty bytes object when the stream is
# fully decompressed.

dec = lzma.LZMADecompressor()
