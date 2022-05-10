import lzma
# Test LZMADecompressor to find out if lzma is available
try:
    lzma.LZMADecompressor()
    lzma_available = True
except NameError:
    lzma_available = False


