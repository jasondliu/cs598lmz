import lzma
# Test LZMADecompressor and LZMACompressor
# Note that LZMADecompressor doesn't support the buffered API yet

# Decompressor

d = lzma.LZMADecompressor()

# Basic operation

assert d.decompress(b"") == b""
