import lzma
# Test LZMADecompressor

lzma_decompressor = lzma.LZMADecompressor()

source = b"XZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00"

# This should be enough to decompress the entire stream
