import lzma
# Test LZMADecompressor.
# Create a known set of compressed input that should match the expected output.
COMPRESSOR = lzma.LZMACompressor()
DATA = b'a' * 1024 + b'b' * 1024 + b'c' * 1024
COMPRESSED = COMPRE
