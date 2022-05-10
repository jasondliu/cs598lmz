import lzma
# Test LZMADecompressor
try:
    lzma.LZMADecompressor()
    LZMA_SUPPORTED = True
except AttributeError:
    LZMA_SUPPORTED = False

