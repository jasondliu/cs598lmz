import lzma
# Test LZMADecompressor

decomp = lzma.LZMADecompressor()

# Try to decompress an empty string
decomp.decompress(b"")

# Decompress a string that's not compressed
