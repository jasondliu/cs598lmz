import lzma
# Test LZMADecompressor.

s = b'\0' * 1000 + b'x' * 1000

d = lzma.LZMADecompressor()

# Decompress some data.
d.decompress(s[:1000])

# Decompress the rest of the data.
