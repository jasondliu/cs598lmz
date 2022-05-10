import lzma
# Test LZMADecompressor

# Test simple decompression

comp = b'X\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\x04\x00\x1b\x04'

decomp = lzma.LZMADecompressor()

