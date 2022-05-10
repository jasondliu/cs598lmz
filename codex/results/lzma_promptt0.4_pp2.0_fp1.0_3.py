import lzma
# Test LZMADecompressor

decomp = lzma.LZMADecompressor()

# Try to decompress an empty string
decomp.decompress(b"")

# Decompress a string that's not compressed
decomp.decompress(b"Hello, world!")

# Decompress a string that's not compressed and has a trailing garbage
decomp.decompress(b"Hello, world!\x00\x00\x00\x00")

# Decompress a string that's not compressed and has a trailing garbage
# that's too long
decomp.decompress(b"Hello, world!\x00\x00\x00\x00\x00\x00\x00\x00")

# Decompress a string that's not compressed and has a trailing garbage
# that's too long
decomp.decompress(b"Hello, world!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Decompress a string that's not
