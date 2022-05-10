import lzma
# Test LZMADecompressor
try:
    lzma.LZMADecompressor()
    lzma_mode = lzma.FORMAT_XZ
except AttributeError:
    lzma_mode = lzma.FORMAT_ALONE
