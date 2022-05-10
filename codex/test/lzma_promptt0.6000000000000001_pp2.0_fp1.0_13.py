import lzma
# Test LZMADecompressor.decompress()

data = b"x" * 100000 + b"y" * 1000
comp = lzma.LZMACompressor()

# Compress and decompress in one step
